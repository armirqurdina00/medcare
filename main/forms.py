from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email address"}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''

class AddPatientForm(forms.ModelForm):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    gender = forms.ChoiceField(required=True, widget=forms.Select(attrs={"class": "form-select"}), label="", choices=GENDER_CHOICES)
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}), label="")

    class Meta:
        model = Patient
        exclude = ("user",)