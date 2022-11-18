from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *


def index(request):
    posts = Post.objects.all()
    if posts:
        return render(request, 'post/index.html', locals())
    else:
        return HttpResponse('no posts yet')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', locals())
