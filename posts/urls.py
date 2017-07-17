from django.conf.urls import url

from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list, name='list'),
    url(r'^create/$', posts_views.post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', posts_views.post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_views.post_delete, name='delete'),
]
