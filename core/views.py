from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,HttpResponse ,redirect
from .forms import NewTodoForm
from .models import Todo
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

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
    paginate_by = 2
    template_name = 'all_todoes.html'
    
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')