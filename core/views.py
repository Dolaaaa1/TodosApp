from django.shortcuts import render ,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_todos(request):
    return render(request,'all_todoes.html')

def add_todos(request):
    return render(request,'new_todo.html')
