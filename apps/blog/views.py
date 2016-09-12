from django.views.generic import ListView
from apps.blog.models import Post


class PostListView(ListView):

    model = Post
    template_name = 'blog/base.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.released()
