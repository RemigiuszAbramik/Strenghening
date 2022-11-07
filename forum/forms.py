from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('name', 'context')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ask Question'}),
            'context': forms.Textarea(attrs={'class': 'form-control'}),
        }