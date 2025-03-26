from django.contrib import admin
from course.models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "school_name", "description", "availability_date", "author", "user", "post_date")
    list_editable = ("school_name", "author")
    sortable_by = ("school_name", "author", "post_date", "category")

admin.site.register(Course, CourseAdmin)