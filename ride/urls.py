from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="posts"),
    path('<int:slug>', views.PostDetail.as_view(), name='post_detail'),
]