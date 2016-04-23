
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'},
        )
    )
    contact_email = forms.EmailField(required=True)
    contact_phone = forms.CharField(required=False)
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': "materialize-textarea"},
        )
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = u"Имя".encode('utf-8')
        self.fields['contact_email'].label = u"Email".encode('utf-8')
        self.fields['contact_phone'].label = u"Телефон (необязательно)".encode('utf-8')
        self.fields['message'].label = u"Сообщение".encode('utf-8')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, anchor='contact'))
