from django.conf.urls import url

from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.posts_home),
]
