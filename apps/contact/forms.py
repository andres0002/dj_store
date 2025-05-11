# py
# django
from django import forms
# third
# own

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Name:', widget=forms.TextInput())
    name.widget.attrs['class'] = 'form-control'
    name.widget.attrs['placeholder'] = 'Name.'
    name.widget.attrs['required'] = 'required'
    email = forms.EmailField(
        label = 'Email:',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email.',
                'required': 'required'
            }
        )
    )
    content = forms.CharField(label = 'Content:', widget=forms.Textarea())
    content.widget.attrs['class'] = 'form-control'
    content.widget.attrs['placeholder'] = 'Content.'
    content.widget.attrs['required'] = 'required'