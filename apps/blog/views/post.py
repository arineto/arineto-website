from django.views.generic import DetailView
from django.views.generic import ListView
from apps.blog.models import Post


__all__ = ['PostListView', 'PostDetailView']


class PostListView(ListView):

    model = Post
    template_name = 'blog/post/post_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.released()


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post/post_details.html'

    def get_context_data(self, **kwargs):
        kwargs = super(PostDetailView, self).get_context_data(**kwargs)
        kwargs['comments'] = self.object.comment_set.exists()
        return kwargs
