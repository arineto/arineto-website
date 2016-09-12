from django.conf.urls import url

from apps.blog import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(),
        name='post_details'),
    url(r'^$', views.PostListView.as_view(), name='home'),
]
