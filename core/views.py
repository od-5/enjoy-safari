# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Setup, Ticket

__author__ = 'alexy'


def home_view(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    return render(request, 'base.html', {
        'setup': setup,
    })

@csrf_exempt
def ticket(request):
    try:
        receoient = Setup.objects.all()[0].email
    except:
        receoient = 'od-5@yandex.ru'
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        ticket = Ticket(name=name, email=email, comment=comment)
        ticket.save()
        if comment:
            message = u'Имя: %s\nE-mail: %s\nСообщение: %s\n' % (name, email, comment)
        else:
            message = u'Имя: %s\nE-mail: %s\n' % (name, email)
        send_mail(
            u'enjoy-safari.ru - Заявка с сайта',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [receoient, ]
        )
        return HttpResponse('true')

    return HttpResponse('fail')
