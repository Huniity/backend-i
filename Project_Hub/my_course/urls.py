from django.urls import path
from django.contrib.auth.views import LoginView
from my_course import views
from django.conf import settings

"""
Defining all views of the main project.
"""

urlpatterns = [
    path("course", views.CourseListView.as_view(), name="course_list"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(), name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name="course_delete"),
    path('update/<int:pk>/', views.CourseEditView.as_view(), name="course_update"),
    path("enroll/<int:pk>/", views.CourseEnrollView.as_view(), name="course_enroll"),
    path("student-courses/", views.StudentEnrolledView.as_view(), name="student_enrolled_courses"),
    path("mentor-courses/", views.MentorCourseView.as_view(), name="mentor_enrolled_courses"),
]