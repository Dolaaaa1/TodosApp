from django.shortcuts import render ,HttpResponse ,redirect
from .forms import NewTodoForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_todos(request):
    return render(request,'all_todoes.html')

def add_todos(request):
    if request.method == 'GET':
        form = NewTodoForm()
        return render(request,'new_todo.html', {'form':form})
    elif request.method == 'POST':
        form = NewTodoForm(request.POST)
        if form.is_valid():
            newTodoItem = form
            newTodoItem.save()
            return redirect('all_todos')
