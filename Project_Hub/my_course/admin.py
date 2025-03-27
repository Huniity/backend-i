from django.contrib import admin
from .models import *

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_title", "category", "school_name", "description", "price", "available_until", "author", "user", "post_date", "enroll_now")
    list_editable = ()
    sortable_by = ("school_name", "author", "post_date", "category")

admin.site.register(Course, CourseAdmin)