from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, logout
from django.shortcuts import redirect
#from course.forms import CourseForm
from course.models import MyCourse

# Create your views here.
class IndexView(TemplateView):
    http_method_names = ["get"]
    template_name = "course/index.html"


class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url = "/"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
     if request.method == "POST":
          logout(request)
          return redirect("/")
     
class CourseListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "/course"
    # form_class = CourseForm
    template_name = "course/course_list.html"

    def get_context_data(self, **kwargs):
        kwargs["object_list"] = MyCourse.objects.filter(user=self.request.user).all()
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)