from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'post/index.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', locals())
