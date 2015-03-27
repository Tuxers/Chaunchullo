from django.shortcuts import render
from django.http import HttpResponse, Http404
from board.models import *
import re
import json

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {
        'posts' : posts,
    })

def get_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except:
        raise Http404('Post no existe')

    return render(request, 'posts/detail.html', {
        'post' : post
    })


def make_post(request):
    title = request.POST['title']
    content = request.POST['content']


    new_post = Post(title=title, content=content)
    found_tags = re.findall('#\S*(?=\s)|#\S*(?=$)', content);
    registered_tags = []

    for tag in found_tags:
        if len(Tag.objects.all().filter(name=tag)) != 0:
            registered_tags.append(tag)

    new_post.save()

    return HttpResponse(json.dumps(registered_tags), content_type="application/json")
