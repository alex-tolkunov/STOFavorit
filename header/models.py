__author__ = 'User'
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Logo(models.Model):
    class Meta():
        db_table = "logo"
        verbose_name = "Заголовок сайта"
        verbose_name_plural = "Заголовок сайта"

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    city = models.CharField(max_length=20, verbose_name="Город")

    def __unicode__(self):
        return self.title

class Contact(models.Model):
    class Meta():
        db_table = "contacts"
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    phone1 = models.CharField(max_length=20, verbose_name="Телефон 1")
    phone2 = models.CharField(max_length=20, verbose_name="Телефон 2")


class ModalContact(models.Model):
    class Meta():
        db_table = "contacts_modal"
        verbose_name = "Контакты Модальное окно"
        verbose_name_plural = "Контакты Модальное окно"

    phone1 = models.CharField(max_length=20, verbose_name="Телефон 1")
    phone2 = models.CharField(max_length=20, verbose_name="Телефон 2")
    email = models.EmailField(verbose_name="E-mail")

