from django.shortcuts import render
from django.http import HttpResponse, Http404
from board.models import *

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {
        'posts' : posts,
    })

def get_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except:
        raise Http404('Post does not exist')

    return render(request, 'posts/detail.html', {
        'post' : post
    })
