from django.contrib import admin
from .models import User, PostForum, ReplyForum


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ReplyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(User, UserAdmin)
admin.site.register(PostForum, PostAdmin)
admin.site.register(ReplyForum, ReplyAdmin)