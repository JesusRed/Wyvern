from django.contrib import admin
from .models import Poster


# Register your models here

class PosterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Poster, PosterAdmin)
