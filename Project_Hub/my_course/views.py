from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, logout, login
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from my_course.models import Course
from my_course.forms import CourseForm
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


"""
Index view for index.html.
"""

class IndexView(TemplateView):
    http_method_names = ["get"]
    template_name = "my_course/index.html"
    logger.info(HttpResponse.status_code)


"""
Signup view for user registration form. User gets a default group "Student" to help him
    search through the website.
"""

class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/course"
    form_class = UserCreationForm

    """
    Setting the student group ass default.
    """

    def form_valid(self, form):
        user = form.save()
        default_group = Group.objects.get(name='Student')
        user.groups.add(default_group)
        login(self.request, user)
        logger.info(f"{form} successfuly created by user")
        return super().form_valid(form)

"""
Logout view helping user to logut from their account and making them be redirected to the homepage.
"""

def logout_view(request):
     if request.method == "POST":
          logout(request)
          return redirect("/")
     logger.info(f"{request} - User successfuly logged out")
     
"""
View to list all the courses available. User can seek through all courses and enroll to which one they want.
Mentors can fill the form instead and see their own posted courses.
"""

class CourseListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "/course"
    form_class = CourseForm
    template_name = "my_course/course_list.html"

    """
    Redirecting user if not auth. Checking if the user is mentor, if yes only displaying their own courses.
    """

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            logger.info(f"{self.request.user} - User not logged in.")
            return redirect("signin")
        if self.request.user.groups.filter(name="Mentor").exists():
            kwargs["mentor_object_list"] = Course.objects.filter(user=self.request.user).all()
            logger.info(f"{self.request.user} - User is mentor. Can create a form")
        else:
            kwargs["object_list"] = Course.objects.all()
            logger.info(f"{self.request.user} - Not a mentor, can only see courses.")
        return super().get_context_data(**kwargs)   

    """
    If form is valid, saving the form in the DB.
    """

    def form_valid(self, form):
            form.instance.user = self.request.user
            logger.info(f"{self.request.user} - Form is valid. Adding form to DB.")
            return super().form_valid(form)
    

    def print_cat(request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        logger.info(f"{request} - Printing categories.")
        return context
    
"""
View that allows mentor users to update an own posted course. All fields are updatable unless postdate and id.
"""

class CourseEditView(UpdateView):
    model = Course
    success_url ="/course"
    fields = [
        "course_title",
        "category",
        "school_name", 
        "description",
        "price",
        "available_until",
        "author",
    ]
    template_name = "my_course/update_confirmation.html"
    
"""
Delete view that allows Mentors to delete their own course.
"""

class CourseDeleteView(DeleteView):
    model = Course
    success_url ="/course"
    template_name = "my_course/delete_confirmation.html"

"""
View that allows users (Students) to enroll to courses posted and available. 
"""

class CourseEnrollView(UpdateView):
    model = Course
    success_url = "/course"
    fields = []
    template_name = "my_course/course_enroll.html"
    
    """
    Checking if the user is enrolled to the course, if not he is added to the variable students that stores the enrolled students.
    """

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        if request.user not in course.students.all():
            course.students.add(request.user)
        logger.info(f"{self.request.user} - Posting Course")
        return redirect("student_enrolled_courses")

"""
View for students to checked all their enrollments. Personalized for each Student user.
"""

class StudentEnrolledView(ListView):
    template_name = "my_course/student_enrolled_courses.html"
    context_object_name = "enrolled_courses"

    def get_queryset(self):
        logger.info(f"{self.request.user} - Accessing Enrolled Course.")
        return self.request.user.enrolled_courses.all()

"""
View that allows mentors to see who is enrolled to their course. Mentors can see the name of all the students.
"""  

class MentorCourseView(ListView):
    template_name = "my_course/mentor_enrolled_courses.html"
    context_object_name = "courses"

    def get_queryset(self):
        logger.info(f"{self.request.user} - Accessing Student Enrolled.")
        return Course.objects.filter(user=self.request.user)