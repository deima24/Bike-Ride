from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filters(status=1).order_by('-created_on')
    template_name = 'index.html'
    #if there is more then 6 then django add page navigation
    paginate_by = 6
