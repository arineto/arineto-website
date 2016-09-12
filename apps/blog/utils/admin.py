from django.contrib import messages
from django.utils import timezone


def release_posts(modeladmin, request, queryset):

    for post in queryset.not_released():
        post.released = True
        post.released_at = timezone.now()
        post.save()

    messages.success(request, 'Posts released with success.')

release_posts.short_description = u'Release posts'
