from django.contrib import admin
from .models import Post, Comment
# Register your models here.

from.models import Post 

class PostAdmin(admin.ModelAdmin):
	list_display = ("title","slug","published","status",)
	list_filter = ("status","created","published","author",)
	search_fields = ("title","body",)
	prepopullated_fields ={"slug":('title',),}
	raw_id_fields = ('author',)
	date_hierarchy = "published"
	ordering = ['status','published',]

class CommentAdmin(admin.ModelAdmin):
	list_display = ("name","post","created","active")
	list_filter = ("active","created","updated")
	search_fields = ("name","body")

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
