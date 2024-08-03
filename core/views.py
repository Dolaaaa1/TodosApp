from django.shortcuts import render ,HttpResponse ,redirect
from .forms import NewTodoForm
from .models import Todo

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_todos(request):
    all_todo = Todo.objects.all().order_by('-id')
    return render(request,'all_todoes.html',{'all_todo':all_todo})

def add_todos(request):
    if request.method == 'GET':
        form = NewTodoForm()
        return render(request,'new_todo.html', {'form':form})
    elif request.method == 'POST':
        form = NewTodoForm(request.POST)
        if form.is_valid():
            newTodoItem = form
            newTodoItem.save()
            return redirect('all_todes')
