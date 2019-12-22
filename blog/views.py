from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Blog, Comment


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'description']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

class MyDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MyDetailView, self).get_context_data(*args, **kwargs)
        context['object_list'] = Post.objects.all()
        return context

# .................................................

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'blog']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # success_url = reverse('post_detail', args=[str(self.id)])

# .................................................

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    fields = ['text']
    # success_url = reverse_lazy('home')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    # прописать
    success_url = reverse_lazy('home')

