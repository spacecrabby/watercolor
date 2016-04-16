from django.shortcuts import render
from landing.forms import ContactForm
# Create your views here.


def landing(request):
    form_class = ContactForm

    return render(request, 'landing.html',
                  {'form': form_class})