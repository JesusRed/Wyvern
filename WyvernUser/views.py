from django.shortcuts import render
from .User import History
from WyvernForum.models import PostForum
from django.shortcuts import redirect


# Create your views here.

def add_post(request, post_id):
    history = History(request)
    post = PostForum.objects.get(id=post_id)

    history.add(post=post)

    return redirect("Forum")


def rem_post(request, post_id):
    history = History(request)
    post = PostForum.objects.get(id=post_id)

    history.rem(post=post)

    return redirect("Forum")


def sub_post(request, post_id):
    history = History(request)
    post = PostForum.objects.get(id=post_id)

    history.sub_post(post=post)

    return redirect("Forum")


def clean_history(request, post_id):
    history = History(request)
    history.clean_history()
    return redirect("Forum")
