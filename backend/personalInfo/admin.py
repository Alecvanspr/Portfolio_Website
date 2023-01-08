from django.contrib import admin
from .models import PersonalInfo, Job, Education, certificate

# Register your models here.
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'about', 'image', 'cv')
    list_filter = ('name', 'email', 'phone', 'address', 'about', 'image', 'cv')
    search_fields = ('name', 'email', 'phone', 'address', 'about', 'image', 'cv')
    ordering = ('name', 'email', 'phone', 'address', 'about', 'image', 'cv')
    filter_horizontal = ()
    list_per_page = 25

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'start_date', 'end_date', 'description', 'image')
    list_filter = ('title', 'company', 'location', 'start_date', 'end_date', 'description', 'image')
    search_fields = ('title', 'company', 'location', 'start_date', 'end_date', 'description', 'image')
    ordering = ('title', 'company', 'location', 'start_date', 'end_date', 'description', 'image')
    filter_horizontal = ()
    list_per_page = 25

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'start_date', 'end_date', 'description', 'image')
    list_filter = ('school', 'degree', 'start_date', 'end_date', 'description', 'image')
    search_fields = ('school', 'degree', 'start_date', 'end_date', 'description', 'image')
    ordering = ('school', 'degree', 'start_date', 'end_date', 'description', 'image')
    filter_horizontal = ()
    list_per_page = 25

class certificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_filter = ('title', 'description', 'date')
    search_fields = ('title', 'description', 'date')
    ordering = ('title', 'description', 'date')
    filter_horizontal = ()
    list_per_page = 25

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(certificate, certificateAdmin)