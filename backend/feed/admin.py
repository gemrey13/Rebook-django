from django.contrib import admin

from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'content', 'image')

admin.site.register(Post, PostAdmin)