from django.db import models
from django.contrib.auth import get_user_model


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_title = models.TextField(blank=False, max_length=100)
    category = models.TextField(blank=False, max_length=100)
    school_name = models.TextField(blank=False, max_length=150)
    description = models.TextField(default="Course description coming soon!")
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2, default=0.00)
    available_until = models.DateField(blank=False)
    author = models.TextField(blank=False, max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    enroll_now = models.BooleanField(null=False, blank=False, default=False)
    
    class Meta:
        db_table = "course_list"
        verbose_name = "Course"
        verbose_name_plural = "Courses"

