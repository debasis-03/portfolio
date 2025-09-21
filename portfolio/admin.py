from django.contrib import admin
from .models import (
    Portfolio, Project, Skill, Technology, 
    Certificate, Recommendation, ContactMessage
)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'category', 'order']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency', 'order']


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'technologies', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['featured', 'order']
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'issue_date', 'order']
    list_filter = ['issue_date', 'issuing_organization']
    search_fields = ['title', 'issuing_organization']
    list_editable = ['order']


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['title', 'recommender_name', 'recommender_company', 'order']
    list_filter = ['recommender_company']
    search_fields = ['title', 'recommender_name', 'recommender_company']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
