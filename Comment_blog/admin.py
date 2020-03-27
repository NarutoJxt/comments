from django.contrib import admin

# Register your models here.
from Comment_blog.models import Article, Comments


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pk","title","content"]
    list_display_links = ["pk","title"]
@admin.register((Comments))
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article","comment"]
    list_display_links = ["article"]