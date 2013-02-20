# -*- coding: utf-8 -*-

from django.template.defaultfilters import stringfilter
from django import template
import re

register = template.Library()

def match_youtube_link(link):
    regex = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
    return regex.match(link)

def match_vk_video(link):
    regex = re.compile(r"^(http://)?(www\.)?(vk\.com/video)?(?P<oid>[0-9]*)_?(?P<id>[0-9]*)")
    return regex.match(link)

@register.filter
@stringfilter
def youtube_vdeo(link):
    match = match_youtube_link(link)
    if not match:
        return ""
    video_id = match.group('id')
    video_preview = """
        <object>
            <param name="movie" value="">
                <param name="allowFullScreen" value="true">
            <param name="allowScriptAccess" value="always">
            <embed src="http://www.youtube.com/v/%s?version=3" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="560" height="315">
        </object>
    """ % video_id
    return video_preview
#youtube_vdeo.is_safe = True # Don't escape HTML

def get_youtube_image(link, alt, size=1):
    """
    0 - big image (120x90);
    1 - small image (480x360).
    """
    match = match_youtube_link(link)
    if not match:
        return ""

    video_id = match.group('id')
    video_preview_image = '<img src="http://img.youtube.com/vi/%s/%d.jpg" alt="%s" />' % (video_id, size, alt)
    return  video_preview_image

@register.filter
@stringfilter
def youtube_preview_image_small(link, alt):
    video_preview_image = get_youtube_image(link, alt)
    return video_preview_image
youtube_preview_image_small.is_safe = True # Don't escape HTML

@register.filter
@stringfilter
def youtube_preview_image_large(link, alt):
    video_preview_image = get_youtube_image(link, alt, size=0)
    return video_preview_image
youtube_preview_image_large.is_safe = True # Don't escape HTML

@register.filter
@stringfilter
def vk_video(link):
    match = match_vk_video(link)
    if not match:
        return ''

    video_preview = """<iframe src="%s" frameborder="0" width="560" height="315"></iframe>""" % link
    return video_preview
vk_video.is_safe = True # Don't escape HTML

