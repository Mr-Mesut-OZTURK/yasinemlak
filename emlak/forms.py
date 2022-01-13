from django import forms
from .models import (
    Message
)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ["cc_myself"]