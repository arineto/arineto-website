from django.views.generic import DetailView
from django.views.generic import ListView
from apps.blog.models import Post


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.released()


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_details.html'
