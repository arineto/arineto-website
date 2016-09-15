from django.conf.urls import url
from django.conf.urls import include

from apps.blog import views

post_patterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(),
        name='post_details'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
]

comment_patterns = [
    url(r'^list/$', views.CommentListView.as_view(), name='comment_list'),
    url(r'^create/$', views.CommentCreateView.as_view(),
        name='comment_create'),
]

urlpatterns = [
    url(r'^', include(post_patterns,)),
    url(r'^comment/', include(comment_patterns,)),
]
