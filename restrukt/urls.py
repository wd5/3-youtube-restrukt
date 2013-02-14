# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from filebrowser.sites import site
from zinnia.sitemaps import TagSitemap, EntrySitemap, CategorySitemap, AuthorSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('zinnia.urls.__init__')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),

    # Сторонние приложения
    url(r'^jsurls.js$', 'django_js_utils.views.jsurls', {}, 'jsurls'),
    url(r'^captcha/', include('captcha.urls')),

    # Всё для админки
    url(r'^grappelli/?', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),
    )

if settings.DEBUG:
    # Обычная админка
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
else:
    # Админка с honeypot'ом
    urlpatterns += patterns('',
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^admin.php', include('admin_honeypot.urls')),
        url(r'^admin-secret/', include(admin.site.urls)),
    )

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap,
}

urlpatterns += patterns('django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
