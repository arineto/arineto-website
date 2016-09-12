from django.views.generic import ListView
from apps.blog.models import Comment


class CommentListView(ListView):

    model = Comment
    template_name = 'blog/comment/comment_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(CommentListView, self).get_queryset()
        post_id = self.request.GET.get('post_id')
        return queryset.filter(post__pk=post_id).order_by('-posted')
