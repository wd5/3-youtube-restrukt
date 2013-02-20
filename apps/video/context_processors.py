# -*- coding: utf-8 -*-

from constance import config
from .models import PostVideoYouTube


def videos_youtuve(request):
    return {
        'videos_youtube_latest': PostVideoYouTube.objects.all()[:config.VIDEO_YOUTUBE_COUNT_AT_HOME_PAGE]
    }