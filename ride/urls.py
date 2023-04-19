from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="posts"),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete/<slug:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('edit/<slug:pk>', views.PostEdit.as_view(), name='post_edit')
]