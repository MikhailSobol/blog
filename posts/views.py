from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
def post_create(request):
    context = {
        'title': 'Create',
    }
    return render(request, "index.html", context)


def post_detail(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    context = {
        'title': instance.title,
        'post': instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'post_queryset': queryset,
        'title': 'List',
    }
    return render(request, "index.html", context)


def post_update(request):
    context = {
        'title': 'Update',
    }
    return render(request, "index.html", context)


def post_delete(request):
    context = {
        'title': 'Delete',
    }
    return render(request, "index.html", context)
