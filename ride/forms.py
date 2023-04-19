from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ A form to create an idea """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'content',
        )
        widgets = {
            'review': SummernoteWidget()
        }