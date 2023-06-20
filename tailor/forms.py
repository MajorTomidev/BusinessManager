from django import forms
from .models import Male, Female, Comment

class MaleForm(forms.ModelForm):
    class Meta:
        model= Male
        fields = '__all__'

class FemaleForm(forms.ModelForm):
    class Meta:
        model= Female
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['name', 'email', 'comment']

