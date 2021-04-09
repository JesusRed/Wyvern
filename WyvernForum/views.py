from django.shortcuts import render, HttpResponse
from .models import ReplyForum, PostForum, User


# Create your views here.

def forum(request):
    replies = ReplyForum.objects.all()
    posts = PostForum.objects.all()
    users = User.objects.all()

    return render(request, "forum.html", {"users": users, "replies": replies, "posts": posts})
