from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_new'),
    path('blog/<int:pk>/', MyDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    # re_path(r'^blog/<int:pk>/post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('comment/new/', CommentCreateView.as_view(), name='comment_new'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]
