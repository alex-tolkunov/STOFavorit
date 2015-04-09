__author__ = 'User'
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Модель слайдер в хэдере
class SlideHead(models.Model):
    class Meta():
        db_table = "slider_head"
        verbose_name = "Слайд"
        verbose_name_plural = "Слайдер Header"

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    photo = models.CharField(max_length=100, verbose_name="Изображение")

    def __unicode__(self):
        return self.title

# список для слайлера в хэдере
class SlideList(models.Model):
    class Meta():
        db_table = "slider_list"
        verbose_name = "Список с описаниями"
        verbose_name_plural = "Список с описаниями"

    list = models.CharField(max_length=255, verbose_name="Описание")
    slide = models.ForeignKey(SlideHead)

    def __unicode__(self):
        return self.list

# Слайдер с отзывами
class SlideReview(models.Model):
    class Meta():
        db_table = "slider_review"
        verbose_name = "Слайд"
        verbose_name_plural = "Слайдер Отзывы"

    text = models.TextField(verbose_name="Текст")
    person = models.CharField(max_length=40, verbose_name="Руководитель")
    organization = models.CharField(max_length=50, verbose_name="Организация")

    def __unicode__(self):
        return self.person

