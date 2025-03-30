from django.contrib import admin
from .models import *

"""
Admin table display in Django administration. Displayed, Editable and Sortable columns.
"""

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_title", "category", "school_name", "description", "price", "available_until", "author", "user", "post_date")
    list_editable = ["available_until"]
    sortable_by = ("school_name", "author", "post_date", "category")

admin.site.register(Course, CourseAdmin)