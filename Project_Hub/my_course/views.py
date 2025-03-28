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

# Create your views here.
class IndexView(TemplateView):
    http_method_names = ["get"]
    template_name = "my_course/index.html"


class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/course"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        default_group = Group.objects.get(name='Student')
        user.groups.add(default_group)
        login(self.request, user)
        return super().form_valid(form)

def logout_view(request):
     if request.method == "POST":
          logout(request)
          return redirect("/")
     
class CourseListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "/course"
    form_class = CourseForm
    template_name = "my_course/course_list.html"

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("signin")
        if self.request.user.groups.filter(name="Mentor").exists():
            kwargs["mentor_object_list"] = Course.objects.filter(user=self.request.user).all()
        else:
            kwargs["object_list"] = Course.objects.all()
        return super().get_context_data(**kwargs)
        
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
    
    def print_cat(request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
    
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
    

class CourseDeleteView(DeleteView):
    model = Course
    success_url ="/course"
    template_name = "my_course/delete_confirmation.html"


class CourseEnrollView(UpdateView):
    model = Course
    success_url = "/course"
    fields = []
    template_name = "my_course/course_enroll.html"
    
    def post(self, request, *args, **kwargs):
        course = self.get_object()
        if request.user not in course.students.all():
            course.students.add(request.user)
        return redirect("student_enrolled_courses")


class StudentEnrolledView(ListView):
    template_name = "my_course/student_enrolled_courses.html"
    context_object_name = "enrolled_courses"

    def get_queryset(self):
        return self.request.user.enrolled_courses.all()
    

class MentorCourseView(ListView):
    template_name = "my_course/mentor_enrolled_courses.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)