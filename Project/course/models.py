from django.db import models
from django.contrib.auth import get_user_model


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    category = models.TextField()
    school_name = models.TextField()
    description = models.TextField()
    availability_date = models.DateField()
    author = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = "listing_course"
        verbose_name = "Course"
        verbose_name_plural = "Courses"

# Create your models here.
