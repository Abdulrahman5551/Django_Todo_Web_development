from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    if request.method == "GET":

        form = TaskForm()
        context = {
        'tasks': tasks,
        'forms': form,
    }
        return render(request, 'todo\list.html', context)

    elif request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'tasks': tasks,
                'forms': form,
                    }
            print("hghghg")
            return render(request, 'todo\list.html', context)
    

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'todo\edit.html', context)

def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)
    context = {
        'item': item,
    }

    if request.method == "GET":
        return render(request, 'todo/delete.html', context)
    
    elif request.method == "POST":
        item.delete()
        return redirect("index")

    