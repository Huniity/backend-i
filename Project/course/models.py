# from django.db import models
# from django.contrib.auth import get_user_model


# class MyCourse(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     course_title = models.TextField()
#     category = models.TextField()
#     school_name = models.TextField()
#     description = models.TextField(default="Course description coming soon!")
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     available_until = models.DateField()
#     author = models.TextField()
#     user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     post_date = models.DateTimeField(auto_now_add=True) 
    
#     class Meta:
#         db_table = "course_listing"
#         verbose_name = "Course"
#         verbose_name_plural = "Courses"

# Create your models here.
