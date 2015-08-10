# coding=utf-8
from django.forms import ModelForm
from .models import Ticket

__author__ = 'alexey'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
