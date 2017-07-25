from django.conf.urls import url

from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.PostListView.as_view(), name='list'),
    url(r'^create/$', posts_views.PostCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', posts_views.PostDetailView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', posts_views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_views.PostDeleteView.as_view(), name='delete'),
]
