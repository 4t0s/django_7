from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo

def list_todo(request):
    if request.method == 'GET':
        tasks = Todo.objects.all()
    elif request.method == 'POST':
        tasks = Todo.objects.filter(title = request.POST.get('title'))
    return render(request, 'list.html', {'tasks': tasks})