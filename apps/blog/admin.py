from django.contrib import admin
from apps.blog.models import Post, Tag, Comment
from apps.blog.utils.admin import release_posts


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'released', 'created_at', 'released_at')
    fields = ('title', 'slug', 'content', 'tags')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-released_at',)
    list_filter = ('released',)
    search_fields = ('title',)
    actions = [release_posts]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Comment)
