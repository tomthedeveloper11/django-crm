from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "John", "class": "form-control", "label": ""}
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Doe", "class": "form-control", "label": ""}
        ),
    )
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "+62852618391", "class": "form-control", "label": ""}
        ),
    )

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "phone")
