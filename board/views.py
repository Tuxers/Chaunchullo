from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from board.models import *

def index(request):
    posts = Post.objects.order_by('-created_at')

    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'posts': posts
    })
    return HttpResponse(template.render(context))

def get_post(request, post_id):
    return HttpResponse('a single post' + post_id)
