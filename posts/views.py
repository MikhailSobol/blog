from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        return _save_instance_and_redirect(form, request, 'Successfully Created')
    if form.errors:
        messages.error(request, 'Not Successfully Created')

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
    return render(request, "posts_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        return _save_instance_and_redirect(form, request, 'Saved')
    if form.errors:
        messages.error(request, 'Not Successfully Updated')

    context = {
        'title': instance.title,
        'post': instance,
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('list')


def _save_instance_and_redirect(form, request, text):
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, text)
    return HttpResponseRedirect(instance.get_absolute_url())
