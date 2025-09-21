from django.core.management.base import BaseCommand
from portfolio.models import Portfolio, Skill, Technology, Project, Certificate, Recommendation


class Command(BaseCommand):
    help = 'Set up sample data for the portfolio website'

    def handle(self, *args, **options):
        self.stdout.write('Setting up sample data...')

        # Create Portfolio
        portfolio, created = Portfolio.objects.get_or_create(
            name="John Doe",
            defaults={
                'title': 'Full Stack Developer',
                'bio': 'I am a passionate full-stack developer with 5+ years of experience building web applications. I love creating innovative solutions and solving complex problems with code.',
                'email': 'john.doe@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA'
            }
        )
        if created:
            self.stdout.write(f'Created portfolio: {portfolio.name}')
        else:
            self.stdout.write(f'Portfolio already exists: {portfolio.name}')

        # Create Technologies
        technologies_data = [
            {'name': 'Python', 'color': '#3776ab'},
            {'name': 'Django', 'color': '#092e20'},
            {'name': 'JavaScript', 'color': '#f7df1e'},
            {'name': 'React', 'color': '#61dafb'},
            {'name': 'HTML5', 'color': '#e34f26'},
            {'name': 'CSS3', 'color': '#1572b6'},
            {'name': 'PostgreSQL', 'color': '#336791'},
            {'name': 'Git', 'color': '#f05032'},
        ]

        for tech_data in technologies_data:
            tech, created = Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults={'color': tech_data['color']}
            )
            if created:
                self.stdout.write(f'Created technology: {tech.name}')

        # Create Skills
        skills_data = [
            {'name': 'Python', 'proficiency': 90, 'category': 'programming', 'order': 1},
            {'name': 'Django', 'proficiency': 85, 'category': 'frameworks', 'order': 2},
            {'name': 'JavaScript', 'proficiency': 80, 'category': 'programming', 'order': 3},
            {'name': 'React', 'proficiency': 75, 'category': 'frameworks', 'order': 4},
            {'name': 'HTML5', 'proficiency': 95, 'category': 'programming', 'order': 5},
            {'name': 'CSS3', 'proficiency': 90, 'category': 'programming', 'order': 6},
            {'name': 'PostgreSQL', 'proficiency': 70, 'category': 'databases', 'order': 7},
            {'name': 'Git', 'proficiency': 85, 'category': 'tools', 'order': 8},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product management, shopping cart, payment processing, and admin dashboard.',
                'short_description': 'Full-featured e-commerce platform with Django and React',
                'technologies': ['Python', 'Django', 'React', 'PostgreSQL'],
                'featured': True,
                'order': 1
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration features, and project tracking capabilities.',
                'short_description': 'Collaborative task management with real-time updates',
                'technologies': ['JavaScript', 'React', 'Node.js', 'MongoDB'],
                'featured': True,
                'order': 2
            },
            {
                'title': 'Portfolio Website',
                'description': 'A responsive portfolio website built with Django, featuring a modern design, admin panel, and contact form functionality.',
                'short_description': 'Responsive portfolio website with Django admin panel',
                'technologies': ['Python', 'Django', 'HTML5', 'CSS3', 'Bootstrap'],
                'featured': True,
                'order': 3
            },
        ]

        for project_data in projects_data:
            tech_names = project_data.pop('technologies')
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add technologies
                for tech_name in tech_names:
                    try:
                        tech = Technology.objects.get(name=tech_name)
                        project.technologies.add(tech)
                    except Technology.DoesNotExist:
                        pass
                self.stdout.write(f'Created project: {project.title}')

        # Create Certificates
        certificates_data = [
            {
                'title': 'AWS Certified Solutions Architect',
                'issuing_organization': 'Amazon Web Services',
                'issue_date': '2023-06-15',
                'description': 'Professional certification for designing distributed systems on AWS'
            },
            {
                'title': 'Django Web Development',
                'issuing_organization': 'Django Software Foundation',
                'issue_date': '2023-03-20',
                'description': 'Advanced Django development techniques and best practices'
            },
        ]

        for cert_data in certificates_data:
            cert, created = Certificate.objects.get_or_create(
                title=cert_data['title'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certificate: {cert.title}')

        # Create Recommendations
        recommendations_data = [
            {
                'title': 'Outstanding Developer Performance',
                'recommender_name': 'Sarah Johnson',
                'recommender_position': 'Senior Engineering Manager',
                'recommender_company': 'Tech Corp Inc.',
                'description': 'John consistently delivered high-quality code and showed excellent problem-solving skills.'
            },
            {
                'title': 'Team Collaboration Excellence',
                'recommender_name': 'Mike Chen',
                'recommender_position': 'Lead Developer',
                'recommender_company': 'StartupXYZ',
                'description': 'John was an invaluable team member who mentored junior developers and contributed to our success.'
            },
        ]

        for rec_data in recommendations_data:
            rec, created = Recommendation.objects.get_or_create(
                title=rec_data['title'],
                defaults=rec_data
            )
            if created:
                self.stdout.write(f'Created recommendation: {rec.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully set up sample data!')
        )
        self.stdout.write('You can now run the development server and visit the admin panel to customize the content.')
