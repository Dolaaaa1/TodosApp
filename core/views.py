from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,HttpResponse ,redirect
from .forms import NewTodoForm
from .models import Todo
from django.views.generic.edit import CreateView ,UpdateView , DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def index(request):
    return render(request,'index.html')


class TodoCreateView(CreateView):
    model = Todo
    fields =['text']
    template_name = 'new_todo.html'
    success_url = '/all/'

class TodoListView(ListView):
    model = Todo
    paginate_by = 3
    template_name = 'all_todoes.html'
    
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')
    
    
class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = ['text']
    template_name = 'update_todo.html'
    success_url = '/all/'
    
class TodoDelete(DeleteView):
    model = Todo
    template_name = 'delete_todo.html'
    success_url = '/all/'
        
    
    