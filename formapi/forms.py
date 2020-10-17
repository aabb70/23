from django import forms

from .models import users

class PostForm(forms.ModelForm):

    class Meta:
        model = users
        fields = ('uid', 'datatest',)