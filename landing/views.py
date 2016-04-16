from django.shortcuts import render, redirect
from landing.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
# Create your views here.


def landing(request):
    form_class = ContactForm

    if request.method == "POST":
        form = form_class(data=request.POST)

        if form.is_valid():

            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_phone = request.POST.get('contact_phone', '')
            message = request.POST.get('message', '')

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
            "New contact form submission",
            content,
            "Your website" + '',
            ['fusee@ya.ru'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('/#contact')

    return render(request, 'landing.html', {'form': form_class})
