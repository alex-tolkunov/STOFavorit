__author__ = 'User'
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class TabItem(models.Model):
    class Meta():
        db_table = "tab_item"
        verbose_name = "Таб"
        verbose_name_plural = "Табы"

    title = models.CharField(max_length=100, verbose_name="Название")

    def __unicode__(self):
        return self.title


class TabItemList(models.Model):
        class Meta():
            db_table = "tab_item_list"
            verbose_name = "Таб"
            verbose_name_plural = "Табы"

        item = models.TextField(verbose_name="Содержание таба")
        link = models.URLField(verbose_name="Ссылка")
        tab = models.ForeignKey(TabItem)

        def __unicode__(self):
            return self.item
