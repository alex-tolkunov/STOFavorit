__author__ = 'User'
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Модель услуги
class Service(models.Model):
    class Meta():
        db_table = "service"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    photo = models.CharField(max_length=100, verbose_name="Изображение", null=True)

    def __unicode__(self):
        return self.title

# Модель подуслуги
class UServices(models.Model):
    class Meta():
        db_table = "uservices"
        verbose_name = "Список услуг"
        verbose_name_plural = "Список услуг"



    MEASURE_CHOICES = (
        (None, 'Нет'),
        ('HOUR', 'Час'),
        ('FLOOR', 'Этаж'),
        ('SMETR', 'Кв.метр'),
        ('DOT', 'Точка'),
        ('ITEM', 'Шт'),
        ('KG', 'Кг'),
        ('L', 'Литр'),
    )

    title = models.CharField(max_length=50, verbose_name="Название")
    price = models.CharField(max_length=20, verbose_name="Цена")
    measure = models.CharField(max_length=10, choices=MEASURE_CHOICES, default=None, verbose_name="Ед. измерения", null=True, blank=True)
    note = models.CharField(max_length="255", verbose_name="Примечание", null=True, blank=True)
    changed = models.BooleanField(default=False, verbose_name="Выбрать услугу")
    service = models.ForeignKey(Service)

    def __unicode__(self):
        return self.title

# Модель для блока Сотрудничество
class Cooperation(models.Model):
    class Meta():
        db_table = 'cooperation'
        verbose_name = "Сотрудничество"
        verbose_name_plural = "Сотрудничество"

    text = models.TextField(verbose_name="Ваш текст")
