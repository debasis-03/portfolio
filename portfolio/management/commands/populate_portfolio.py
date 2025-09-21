from django.core.management.base import BaseCommand
from django.utils import timezone
from portfolio.models import Portfolio, Skill, Technology, Project
from datetime import date


class Command(BaseCommand):
    help = 'Populate the portfolio with sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate portfolio data...'))

        # Create or update portfolio
        portfolio, created = Portfolio.objects.get_or_create(
            defaults={
                'name': 'John Doe',
                'title': 'Full Stack Developer & UI/UX Designer',
                'bio': 'Passionate full-stack developer with 5+ years of experience in creating modern web applications. I specialize in React, Django, and cloud technologies. Always eager to learn new technologies and solve complex problems.',
                'email': 'john.doe@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Portfolio created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Portfolio already exists'))

        # Create technologies
        technologies_data = [
            {'name': 'Python', 'color': '#3776ab'},
            {'name': 'Django', 'color': '#092e20'},
            {'name': 'React', 'color': '#61dafb'},
            {'name': 'JavaScript', 'color': '#f7df1e'},
            {'name': 'HTML5', 'color': '#e34f26'},
            {'name': 'CSS3', 'color': '#1572b6'},
            {'name': 'Bootstrap', 'color': '#7952b3'},
            {'name': 'PostgreSQL', 'color': '#336791'},
            {'name': 'MongoDB', 'color': '#47a248'},
            {'name': 'AWS', 'color': '#ff9900'},
            {'name': 'Docker', 'color': '#2496ed'},
            {'name': 'Git', 'color': '#f05032'},
        ]

        for tech_data in technologies_data:
            tech, created = Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults={'color': tech_data['color']}
            )
            if created:
                self.stdout.write(f'Created technology: {tech.name}')

        # Create skills
        skills_data = [
            {'name': 'Python', 'proficiency': 95, 'category': 'programming'},
            {'name': 'JavaScript', 'proficiency': 90, 'category': 'programming'},
            {'name': 'Django', 'proficiency': 92, 'category': 'frameworks'},
            {'name': 'React', 'proficiency': 88, 'category': 'frameworks'},
            {'name': 'PostgreSQL', 'proficiency': 85, 'category': 'databases'},
            {'name': 'MongoDB', 'proficiency': 80, 'category': 'databases'},
            {'name': 'AWS', 'proficiency': 75, 'category': 'tools'},
            {'name': 'Docker', 'proficiency': 82, 'category': 'tools'},
            {'name': 'UI/UX Design', 'proficiency': 78, 'category': 'other'},
            {'name': 'Project Management', 'proficiency': 85, 'category': 'other'},
        ]

        for i, skill_data in enumerate(skills_data):
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'proficiency': skill_data['proficiency'],
                    'category': skill_data['category'],
                    'order': i
                }
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create sample projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product catalog, shopping cart, payment integration, and admin dashboard.',
                'short_description': 'Full-featured e-commerce platform with Django backend and React frontend.',
                'featured': True,
                'technologies': ['Python', 'Django', 'React', 'PostgreSQL', 'Bootstrap'],
                'order': 1
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration features, and project tracking capabilities.',
                'short_description': 'Collaborative task management app with real-time updates and team features.',
                'featured': True,
                'technologies': ['JavaScript', 'React', 'MongoDB', 'CSS3'],
                'order': 2
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A responsive weather dashboard that displays current weather conditions and forecasts for multiple cities with beautiful visualizations.',
                'short_description': 'Responsive weather dashboard with forecasts and visualizations.',
                'featured': True,
                'technologies': ['JavaScript', 'HTML5', 'CSS3', 'Bootstrap'],
                'order': 3
            },
            {
                'title': 'Portfolio Website',
                'description': 'A modern, responsive portfolio website built with Django, featuring a clean design and smooth animations.',
                'short_description': 'Modern portfolio website with clean design and animations.',
                'featured': False,
                'technologies': ['Python', 'Django', 'HTML5', 'CSS3'],
                'order': 4
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'short_description': project_data['short_description'],
                    'featured': project_data['featured'],
                    'order': project_data['order']
                }
            )
            
            if created:
                # Add technologies to project
                for tech_name in project_data['technologies']:
                    try:
                        tech = Technology.objects.get(name=tech_name)
                        project.technologies.add(tech)
                    except Technology.DoesNotExist:
                        pass
                
                self.stdout.write(f'Created project: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated portfolio with sample data!')
        )
