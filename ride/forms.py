from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ A form to create an idea """
    class Meta:
        model = Idea
        fields = (
            
        )
        widgets = {
            'review': SummernoteWidget()
        }