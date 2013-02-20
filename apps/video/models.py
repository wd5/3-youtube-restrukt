# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from zinnia.models.entry import Entry


class PostVideoYouTube(models.Model):
    post = models.ForeignKey(Entry, verbose_name='Пост')
    name = models.CharField('Название', max_length=64)
    link = models.URLField('Ссылка на видео', help_text='Например: http://www.youtube.com/watch?v=3nbKqgpVADk')
    priority = models.PositiveIntegerField('Приоритет вывода', default=0)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)

    class Meta:
        ordering = ()
        verbose_name = 'Ссылка на видео'
        verbose_name_plural = 'Видео c YouTube'
