from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Portfolio(models.Model):
    """Main portfolio information"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_image = models.FileField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Skills with proficiency levels"""
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Proficiency level from 1 to 100"
    )
    category = models.CharField(max_length=50, choices=[
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & Technologies'),
        ('databases', 'Databases'),
        ('other', 'Other'),
    ])
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for homepage")
    image = models.FileField(upload_to='projects/')
    live_url = models.URLField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField('Technology', blank=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Technology(models.Model):
    """Technology tags for projects"""
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#007bff', help_text="Hex color code")

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Certificate(models.Model):
    """Professional certificates"""
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')
    certificate_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"


class Recommendation(models.Model):
    """Letters of recommendation"""
    title = models.CharField(max_length=200)
    recommender_name = models.CharField(max_length=100)
    recommender_position = models.CharField(max_length=200)
    recommender_company = models.CharField(max_length=200)
    letter_file = models.FileField(upload_to='recommendations/')
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'recommender_name']

    def __str__(self):
        return f"{self.title} - {self.recommender_name}"


class ContactMessage(models.Model):
    """Contact form messages"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
