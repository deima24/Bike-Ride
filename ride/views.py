from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm
from django.views.generic import (CreateView,DetailView, ListView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.template.defaultfilters import slugify

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "rides.html"
    #if there is more then 6 then django add page navigation
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post =  get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



class PostCreate(CreateView):
    """ A view to create an post """

    form_class = PostForm
    template_name = 'create_post.html'
    success_url = "/posts/"
    model = Post

    def form_valid(self, form):
        """ If form is valid return to browse pots """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, 'Post created successfully')
        return super(PostCreate, self).form_valid(form)

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an post """
    model = Post
    success_url = "/posts/"
    template_name = "post_delete.html"

    def test_func(self):
        return self.request.user == self.get_object().author


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A view to edit an idea """

    Model = Post
    form_class = PostForm
    success_url = "/posts/"
    template_name = "post_edit.html"
    queryset = Post.objects

    def form_valid(self, form):
        """ If form is valid return to browse ideas"""
        self.success_url + str(self.object.pk) + '/'
        messages.success(self.request, 'Post updated successfully')
        return super().form_valid(form) 

    def test_func(self):
        """ A function to test if the user is the author """
        return self.request.user == self.get_object().author