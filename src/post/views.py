from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def allPosts(request):
    allposts = Post.objects.all()
    return render(request, 'allPosts.html', {'allposts': allposts})


@login_required
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


@login_required
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


@login_required
def like_post(request, postID):
    post = Post.objects.get(id=postID)
    if not request.user in post.liked_users.all():
        post.likes += 1
        post.liked_users.add(request.user)
        post.save()
        return redirect('posts')
    else:
        return redirect('posts')


@login_required
def comment_post(request, postID):
    post = Post.objects.get(id=postID)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('comments', postID=postID)
    else:
        comments = Comment.objects.filter(post=post)
        form = CommentForm()
        return render(request, 'comments.html', {'comments': comments, 'form': form,
                                                 'action': '/post/comments/{}/'.format(post.id)})


@login_required
def share_post(request, postID):
    post = Post.objects.get(id=postID)
    if request.method == "POST":
        title = request.POST['title']
        shared_post = post
        new_post = Post.objects.create(
            user=request.user, shared_post=shared_post, title=title)
        post.share_count += 1
        post.save()
        return redirect('posts')
    else:
        return render(request, 'share.html', {'action': '/post/share/{}/'.format(post.id), 'post': post})
