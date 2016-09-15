from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from apps.blog.forms import CommentForm
from apps.blog.models import Comment
from apps.blog.models import Post


__all__ = ['PostListView', 'PostDetailView', 'CommentListView']


class PostListView(ListView):

    model = Post
    template_name = 'blog/post/post_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.released()


class PostDetailView(CreateView):

    form_class = CommentForm
    template_name = 'blog/post/post_details.html'

    def get_form_kwargs(self):
        kwargs = super(PostDetailView, self).get_form_kwargs()
        kwargs['post'] = Post.objects.get(slug=self.kwargs['slug'])
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(PostDetailView, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=self.kwargs['slug'])
        kwargs['comments'] = post.comment_set.exists()
        kwargs['object'] = post
        return kwargs

    def get_success_url(self):
        post = Post.objects.get(slug=self.kwargs['slug'])
        return reverse('blog:post_details', args=(post.slug,))


class CommentListView(ListView):

    model = Comment
    template_name = 'blog/comment/comment_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(CommentListView, self).get_queryset()
        post_id = self.request.GET.get('post_id')
        return queryset.filter(post__pk=post_id).order_by('-posted')
