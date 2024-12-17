from django import forms
from .models import Appointment
from .models import ContactSubmission

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'email',
            'phone',
            'preferred_date',
            'preferred_time',
            'appointment_type',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Message'})
        self.fields['preferred_date'].widget.attrs.update({
            'class': 'datepicker',
            'placeholder': 'Select a date'
        })
        self.fields['preferred_time'].widget.attrs.update({
            'class': 'timepicker',
            'placeholder': 'Select a time'
        })
        self.fields['appointment_type'].widget.attrs.update({'placeholder': 'Appointment type'})



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter your Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter a valid email address'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Enter your message', 'rows': 4})
