from django.conf.urls import url

from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list),
    url(r'^create/$', posts_views.post_create),
    url(r'^(?P<id>\d+)/$', posts_views.post_detail, name='detail'),
    url(r'^update/$', posts_views.post_update),
    url(r'^delete/$', posts_views.post_delete),
]
