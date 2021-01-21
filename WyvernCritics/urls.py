from django.urls import path
from WyvernCritics import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('posters', views.posters, name="Posters"),
    path('critics', views.critics, name="Critics"),
    path('forum', views.forum, name="Forum"),
    path('contact', views.contact, name="Contact"),
]