from django.urls import path
from WyvernForum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.forum, name="Forum"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
