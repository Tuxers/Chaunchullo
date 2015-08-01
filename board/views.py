import os
import magic
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from board.models import *
from board.utils import save_uploaded_file
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
    try:
        title = request.POST['title']
        content = request.POST['content']
        if request.method == 'POST' and request.FILES:
            file_name = save_uploaded_file(request.FILES['file'])
        new_post = Post(title=title, content=content)
        new_post.save()

        new_file = File(path=file_name, post=new_post)
        new_file.save()
    except Exception as e:
        return HttpResponseRedirect('/error')

    return HttpResponseRedirect('/')

def download_file(request, file_name):
    path = '/home/donkeysharp/tmp/' + file_name
    if os.path.exists(path):
        response = HttpResponse()
        f = open(path)
        mime = magic.Magic(mime=True)
        response['Content-type'] = mime.from_file(path)
        response.content = f.read()
        f.close()

        return response
    else:
        raise Http404('Archivo no existe')

    new_post = Post(title=title, content=content)
    found_tags = re.findall('#\S*(?=\s)|#\S*(?=$)', content);
    registered_tags = []

    for tag in found_tags:
        if len(Tag.objects.all().filter(name=tag)) != 0:
            registered_tags.append(tag)

    new_post.save()

    return HttpResponse(json.dumps(registered_tags), content_type="application/json")
