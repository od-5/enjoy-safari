# coding=utf-8
from django.db import models

__author__ = 'alexey'

class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)


class Ticket(Common):

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'core'

    def __unicode__(self):
        return self.name

    def performed_at(self):
        pass

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Отклонена'),
        (3, u'Нет ответа'),
    )

    SALE_STATUS_CHOICE = (
        (0, u'Ожидание оплаты'),
        (1, u'Уточнение деталей'),
        (2, u'Оплачено'),
    )

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    email = models.EmailField(verbose_name=u'e-mail', max_length=256)
    comment = models.TextField(verbose_name=u'Сообщение клиента', blank=True, null=True)
    sale = models.BooleanField(verbose_name=u'Продажа', default=False)
    ticket_status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE, default=0, blank=True, null=True)
    ticket_comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)

    travel_start = models.DateField(verbose_name=u'Начало тура', blank=True, null=True)
    travel_end = models.DateField(verbose_name=u'Конец тура', blank=True, null=True)
    sale_status = models.PositiveSmallIntegerField(verbose_name=u'Статус продажи', choices=SALE_STATUS_CHOICE, default=0, blank=True, null=True)
    sale_comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name=u'Сумма', default=0, blank=True, null=True)
    commission = models.PositiveIntegerField(verbose_name=u'Коммисия', default=0, blank=True, null=True)
    total_price = models.PositiveIntegerField(verbose_name=u'Итого', default=0, blank=True, null=True)


class Setup(models.Model):
    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    video = models.TextField(verbose_name=u'HTML-код видео', blank=True, null=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'core'