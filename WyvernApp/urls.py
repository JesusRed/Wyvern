from django.urls import path
from WyvernApp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('general', views.critics, name="Critics"),
    path('forum', views.forum, name="Forum"),
    path('contact', views.contact, name="Contact"),
]