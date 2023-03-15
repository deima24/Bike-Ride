from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    #Creates slug name from the title
    prepopulated_fields = {'slug': ('title',)}

    #adds filter to see status of the post and date
    list_filter = ['status', 'created_on']

    #Shows the title , slug , status and when the post was created
    list_display = ('title', 'slug', 'status', 'created_on')

    #Adds a search field so you can search post by the title or content
    search_fields = ('title', 'content')
    summernote_fields = ('content')

# Creating comment admin page to manage it
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email address', 'body')
    actions = ['approve_comments']

    # Post request to be approved
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
