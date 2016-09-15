from django.views.generic import CreateView
from django.views.generic import ListView
from apps.blog.models import Post
from apps.blog.models import Comment
from apps.blog.forms import CommentForm


class CommentListView(ListView):

    model = Comment
    template_name = 'blog/comment/comment_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(CommentListView, self).get_queryset()
        post_id = self.request.GET.get('post_id')
        return queryset.filter(post__pk=post_id).order_by('-posted')


class CommentCreateView(CreateView):

    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment/comment_form.html'

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        if 'post_id' in self.request.GET:
            post_id = self.request.GET.get('post_id')
            kwargs['post'] = Post.objects.get(pk=post_id)
        return kwargs
