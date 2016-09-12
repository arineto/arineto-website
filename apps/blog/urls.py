from django.conf.urls import url

from apps.blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='home'),
]
