from django.contrib import admin
from .models import Role, Person, Movie, Review


# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Role, RoleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
