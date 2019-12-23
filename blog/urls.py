from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_new'),
    path('blog/<int:pk>/', MyDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),

    # <p><a href="{% url 'post_new' blog.pk  %}">+ Добавить пост</a></p> blog_detail
    path('blog/<int:pk>/post/new/', PostCreateView.as_view(), name='post_new'),
    url(r'^blog/(?P<pk>\d+)/post/(?P<post_pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^blog/(?P<pk>\d+)/post/(?P<post_pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_edit'),
    url(r'^blog/(?P<pk>\d+)/post/(?P<post_pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete'),

    # path('comment/<int:pk>/new', CommentCreateView.as_view(), name='comment_new'),
    # url(r'^blog/(?P<pk>\d+)/post/(?P<post_pk>\d+)/comment/(?P<comment_pk>\d+)/edit$', CommentUpdateView.as_view(), name='post_edit'),

    url(r'^blog/(?P<pk>\d+)/post/(?P<post_pk>\d+)/comment/new', CommentCreateView.as_view(), name='comment_new'),

    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]
