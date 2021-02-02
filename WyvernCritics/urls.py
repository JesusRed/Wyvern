from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.critics, name="Critics"),
    path('director/<int:person_id>/', views.director, name="Director"),
]
