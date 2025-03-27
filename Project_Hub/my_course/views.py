from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, logout, login
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
        
        # if self.request.user.groups.filter(name="Mentor").exists(): #mentor checking group
        #     kwargs["mentor_course"] = Course.objects.filter(author=self.request.user) #only prints his course
        # else:
        #     kwargs["object_list"] = Course.objects.all() #prints course for students
        # return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
    
class CourseEditView():
    pass

class CourseDeleteView():
    pass