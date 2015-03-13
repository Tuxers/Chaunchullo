from django.shortcuts import render
from django.http import HttpResponse
from board.models import *

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {
        'posts' : posts
    })

def get_post(request, post_id):
    return HttpResponse('a single post' + post_id)
