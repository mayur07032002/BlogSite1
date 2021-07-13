from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
import random
def index(request):
    if request.method=='POST':
        query=request.POST.get('search')
        if len(query)>75 or query=="":
            posts=Post.object.none()
        else:
            post_title=Post.objects.filter(title__icontains=query)
            post_content=Post.objects.filter(content__icontains=query)
            post_author=Post.objects.filter(author__icontains=query)
            posts=(post_title.union(post_content)).union(post_author)
        context={'posts':posts,'num_posts':len(posts)}
        return render(request,'bloghome.html',context)

    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'bloghome.html',context)


def write(request):
    if request.method=='POST':
        title=request.POST.get('title')
        slug=str(random.randint(100,1000000))
        content=request.POST.get('content')
        print(content)
        author=request.user.username
        post=Post(author=author ,title=title,slug=slug,content=content)
        post.save()
        return redirect("BlogHome")
    else:
        return render(request,'writeblog.html')

def viewblog(request,slug):
    post=Post.objects.filter(slug=slug)[0]
    return render(request,'blogpost.html',{'post':post})