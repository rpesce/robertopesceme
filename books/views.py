from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from books.models import Post


def PostListView(request):
    posts = Post.objects.all()
    for post in posts:
        post.count_votes()
        post.count_comments()

    context = {
        'posts': posts,
    }

    return render(request, 'books/postlist.html', context)

def NewPostListView(request):
    posts = Post.objects.all().order_by('-created_on')
    for post in posts:
        post.count_votes()
        post.count_comments()

    context = {
        'posts': posts,
    }

    return render(request, 'books/postlist.html', context)

def PastPostListView(request):
    time = str((datetime.now(tz=timezone.utc) - timedelta(minutes=30)))
    # __lte stands for less than or equal
    posts = Post.objects.filter(created_on__lte=time)
    for post in posts:
        post.count_votes()
        post.count_comments()

    context = {
        'posts': posts,
    }

    return render(request, 'books/postlist.html', context)
