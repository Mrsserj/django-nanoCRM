# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    name = models.CharField(verbose_name=u'Название', max_length=255)
    photo = models.FileField(upload_to='photo', verbose_name=u'Фото', blank=True, null=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=50, blank=True, null=True)
    mob_phone = models.CharField(verbose_name=u'Сотовый', max_length=50, blank=True, null=True)
    other_phone = models.CharField(verbose_name=u'Дополнительный телефон', max_length=50, blank=True, null=True)
    email = models.CharField(verbose_name=u'E-mail', max_length=50, blank=True, null=True)
    skype = models.CharField(verbose_name=u'Skype', max_length=50, blank=True, null=True)
    note = models.TextField(verbose_name=u'Примечание', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.name, self.user.last_name)

    class Meta:
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'

class Calendar(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=u'Клиент')
    _type = models.IntegerField(verbose_name=u'Тип события', blank=True, null=True)
    name = models.CharField(verbose_name=u'Название', max_length=255)
    cd = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
    dt = models.DateTimeField(verbose_name=u'Дата события')
    notify = models.IntegerField(verbose_name=u'Уведомлять за', blank=True, null=True)
    notify_list = models.TextField(verbose_name=u'Список уведомления', blank=True, null=True)
    duration = models.IntegerField(verbose_name=u'Продолжительность события', blank=True, null=True)
    place = models.CharField(verbose_name=u'Место', max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.customer.name)

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

