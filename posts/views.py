from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View

from .models import Post
from .forms import PostForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'homepage.html', {})


class PostCreateView(View):
    def get(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        return render(request, 'post_form.html', {
                'form': form, 
            })

    def post(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            return _save_instance_and_redirect(form, request, '')
            
            
class PostDetailView(View):
    def get(self, request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        context = {
        'title': instance.title,
        'post': instance,
        'request': request,
        }
        return render(request, "post_detail.html", context)



class PostListView(View):
    def get(self, request):
        queryset_list = Post.objects.all()
        most_read = queryset_list[:3]
        paginator = Paginator(queryset_list, 9)

        page = request.GET.get('page')

        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {
            'post_queryset': queryset,
            'most_read': most_read,
            'title': 'List',
            'request': request,
        }
        return render(request, "posts_list.html", context)


class PostDeleteView(View):
    def get(self, request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        instance.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('list')


def _save_instance_and_redirect(form, request, text):
    instance = form.save(commit=False)
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
