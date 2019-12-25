from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Blog, Comment

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['object_list'] = Post.objects.all().filter(blog=context['blog'])
        return context

# .................................................

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'post_pk'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['comment_list'] = Comment.objects.all().filter(post=self.kwargs['post_pk'])
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(PostCreateView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk'], })


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    pk_url_kwarg = 'post_pk'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    pk_url_kwarg = 'post_pk'

    def get_success_url(self):
        blog = self.object.blog
        return reverse_lazy('blog_detail', kwargs={'pk': blog.id})

# .................................................

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ['text']
    pk_url_kwarg = 'comment_pk'

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk'], 'post_pk': self.kwargs['post_pk'], })


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    fields = ['text']
    pk_url_kwarg = 'comment_pk'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk'], 'post_pk': self.kwargs['post_pk'], })


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    pk_url_kwarg = 'comment_pk'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk'], 'post_pk': self.kwargs['post_pk'], })


