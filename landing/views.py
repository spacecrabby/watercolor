
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from landing.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage

# Create your views here.


def landing(request):
    form = ContactForm
    context = {}

    if request.method == "POST":
        form = form(data=request.POST)

        if form.is_valid():

            contact_name = request.POST.get('contact_name', '').encode('utf-8')
            contact_email = request.POST.get('contact_email', '').encode('utf-8')
            contact_phone = request.POST.get('contact_phone', '').encode('utf-8')
            message = request.POST.get('message', '').encode('utf-8')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')


            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                u"Новая заявка на курсы",
                content,
                'info@watercolorsketching.ru',
                ['info@watercolorsketching.ru'],
                reply_to=[contact_email],
            )
            email.send()
            return redirect('/success')
        else:
            context['anchor'] = 'contact'

    context['form'] = form

    return render(request, 'landing.html', context)


def success(request):
    return render(request, 'success.html')
