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
        required=True,
        widget=forms.Textarea(
            attrs={'class': "materialize-textarea"},
        )
    )
