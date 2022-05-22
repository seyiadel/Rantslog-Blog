from django.contrib import admin
from .models import Blogpost,Category,Comment

class CommentInline(admin.TabularInline):
    model= Comment 
    raw_id_fields=['post']

# Register your models here.
class BlogpostAdmin(admin.ModelAdmin):

    search_fields =['title', 'intro', 'body']
    list_display=['title', 'slug','category','created_at','status']
    list_filter=['category', 'created_at','status']
    inlines=[CommentInline]
    prepopulated_fields={'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields=['title']
    list_display =['title',]
    prepopulated_fields= {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'comment','post', 'created_at']





admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)