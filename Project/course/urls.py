from django.urls import path
from django.contrib.auth.views import LoginView
from course import views
from django.conf import settings

urlpatterns = [
    path("course", views.CourseListView.as_view(), name="course_list"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(), name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
]