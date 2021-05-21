from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .favs import Favs
from .models import ReplyForum, PostForum, User



# Create your views here.

def new_fav(request, comment_id):
    favs = Favs(request)
    comment=PostForum.objects.get(id=comment_id)
    favs.add(comment=comment)

    return redirect("forum")

def del_fav(request, comment_id):
    favs = Favs(request)
    comment=PostForum.objects.get(id=comment_id)
    favs.delete_favs(comment=comment)
    
    return redirect("forum")

def del_fav(request, comment_id):
    favs = Favs(request)
    comment=PostForum.objects.get(id=comment_id)
    favs.less_favs(comment=comment)
    
    return redirect("forum")

def clean_favs(request, comment_id):
    favs = Favs(request)
    favs.clean_favs()
    
    return redirect("forum")



def forum(request):
    replies = ReplyForum.objects.all()
    posts = PostForum.objects.all()
    users = User.objects.all()

    return render(request, "forum.html", {"users": users, "replies": replies, "posts": posts})
