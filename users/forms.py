from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)
    id_no = forms.CharField(label='ID No.', max_length=20)
    phone_no = forms.CharField(label='Phone No.', max_length=20)
    cgpa = forms.CharField(label='CGPA', max_length=20)
    degree = forms.CharField(label='Degree', max_length=20)
    stream = forms.CharField(label='Stream', max_length=20)
    class Meta:
        model = Profile
        fields = ['first_name','last_name','id_no','phone_no','cgpa','degree','stream','image']

class ProfileViewForm(forms.ModelForm):
    placed_in = forms.CharField(label='Job Offered In...(you can not change this field)', max_length=20)
    class Meta:
        model = Profile
        fields = ['placed_in']