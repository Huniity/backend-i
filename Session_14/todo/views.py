from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo":"World", "tasks":tasks})

class TaskListView(ListView):
    model = Task
