from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.order_by('-id')
    context = {'title': 'Главная страница', 'tasks': task}

    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неправильно.'

    form = TaskForm()
    context = {'form': form,
               'error': error
               }
    return render(request, "main/create.html", context)
