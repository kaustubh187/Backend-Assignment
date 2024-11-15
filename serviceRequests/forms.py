from django import forms
from .models import ServiceRequest
from django.contrib.auth.models import User


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'attachment']

class UserSignupForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('support_rep', 'Support Representative'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='Sign Up As')
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }


class UpdateServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']  # Add any other fields you want to update