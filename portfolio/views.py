from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from .models import (
    Portfolio, Project, Skill, Technology, 
    Certificate, Recommendation, ContactMessage
)
from .forms import ContactForm


def home(request):
    """Homepage view"""
    try:
        portfolio = Portfolio.objects.first()
    except Portfolio.DoesNotExist:
        portfolio = None
    
    featured_projects = Project.objects.filter(featured=True).order_by('order')[:3]
    all_projects = Project.objects.all().order_by('order')[:6]
    skills = Skill.objects.all().order_by('order', 'name')[:8]
    
    context = {
        'portfolio': portfolio,
        'featured_projects': featured_projects,
        'all_projects': all_projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """About page view"""
    try:
        portfolio = Portfolio.objects.first()
    except Portfolio.DoesNotExist:
        portfolio = None
    
    skills = Skill.objects.all().order_by('order', 'name')
    certificates = Certificate.objects.all().order_by('order', '-issue_date')
    recommendations = Recommendation.objects.all().order_by('order', 'recommender_name')
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        category = skill.category
        if category not in skill_categories:
            skill_categories[category] = []
        skill_categories[category].append(skill)
    
    context = {
        'portfolio': portfolio,
        'skill_categories': skill_categories,
        'certificates': certificates,
        'recommendations': recommendations,
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    """Projects page view"""
    projects = Project.objects.all().order_by('order', '-created_at')
    technologies = Technology.objects.all().order_by('name')
    
    # Filter by technology if specified
    selected_tech = request.GET.get('tech')
    if selected_tech:
        projects = projects.filter(technologies__name__icontains=selected_tech)
    
    context = {
        'projects': projects,
        'technologies': technologies,
        'selected_tech': selected_tech,
    }
    return render(request, 'portfolio/projects.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = form.save()
            
            # Send email (in production, you'd configure proper email settings)
            try:
                send_mail(
                    f'New Contact Message from {contact_message.name}',
                    f'Name: {contact_message.name}\nEmail: {contact_message.email}\nMessage: {contact_message.message}',
                    settings.EMAIL_HOST_USER,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)


def project_detail(request, project_id):
    """Project detail view"""
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found.')
        return redirect('projects')
    
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)


@require_http_methods(["GET"])
def filter_projects(request):
    """AJAX endpoint for filtering projects by technology"""
    tech_name = request.GET.get('tech', '')
    
    if tech_name:
        projects = Project.objects.filter(technologies__name__icontains=tech_name).order_by('order', '-created_at')
    else:
        projects = Project.objects.all().order_by('order', '-created_at')
    
    projects_data = []
    for project in projects:
        projects_data.append({
            'id': project.id,
            'title': project.title,
            'short_description': project.short_description,
            'image_url': project.image.url if project.image else '',
            'live_url': project.live_url,
            'source_url': project.source_url,
            'technologies': [{'name': tech.name, 'color': tech.color} for tech in project.technologies.all()],
        })
    
    return JsonResponse({'projects': projects_data})
