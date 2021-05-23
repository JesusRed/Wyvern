from django.urls import path
from WyvernForum import favs, views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.forum, name="Forum"),
    path('add/<int:comment_id>/', views.new_fav, name="Add"),
]
