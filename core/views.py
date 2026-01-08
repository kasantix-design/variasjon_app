from django.shortcuts import render, get_object_or_404
from .models import Task, BrainDumpItem, TaskList

def home_view(request):
    return render(request, 'home.html')

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def brain_dump_view(request):
    items = BrainDumpItem.objects.all()
    return render(request, 'brain_dump.html', {'items': items})

def tasklist_view(request, list_id):
    tasklist = get_object_or_404(TaskList, id=list_id)
    return render(request, 'tasklist.html', {'tasklist': tasklist})