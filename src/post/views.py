from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.


def allPosts(request):
    allposts = Post.objects.all()
    return render(request, 'allPosts.html', {'allposts': allposts})


def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponse('created Post')
        else:
            return render(request, 'addPost.html', {'btn': 'create', 'form': form, 'form_errors': form.errors, 'action': '/post/add/'})
    else:
        form = PostForm()
        return render(request, 'addPost.html', {'btn': 'create', 'form': form, 'action': '/post/add/'})


def editPost(request, postID):
    instance = Post.objects.get(id=postID)
    if request.user == instance.user:
        form = PostForm(request.POST or None,
                        request.FILES or None, instance=instance)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('created Post')
        else:
            return render(request, 'addPost.html', {'btn': 'update', 'form': form, 'form_errors': form.errors, 'action': '/post/edit/{}/'.format(instance.id)})
    else:
        return HttpResponse('u didnT create this post')
