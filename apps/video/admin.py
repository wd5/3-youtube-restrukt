# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import PostVideoYouTube


class PostVideoYouTubeAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'pub_date', 'post', 'link')
    list_editable = ('priority', 'pub_date', 'post')
    search_fields = ('name', )
    list_filter = ('post', 'priority', 'pub_date')

admin.site.register(PostVideoYouTube, PostVideoYouTubeAdmin)
