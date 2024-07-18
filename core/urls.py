from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'),
    path('all/', all_todos , name='all_todes'),
    path('add/', add_todos , name='add_todo'),
    

]