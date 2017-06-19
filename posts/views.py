from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        return _save_instance_and_redirect(form)

    context = {
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
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


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        return _save_instance_and_redirect(form)

    context = {
        'title': instance.title,
        'post': instance,
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_delete(request):
    context = {
        'title': 'Delete',
    }
    return render(request, "index.html", context)


def _save_instance_and_redirect(form):
    instance = form.save(commit=False)
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
