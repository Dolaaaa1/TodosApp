from django.forms import ModelForm
from .models import Todo

class NewTodoForm(ModelForm):
    class Meta :
        model =Todo
        fields = ('text',)  