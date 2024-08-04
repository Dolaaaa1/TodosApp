from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'),
    path('all/',TodoListView.as_view(), name='all_todes'),
    path('add/',TodoCreateView.as_view() , name='add_todo'),
    

]