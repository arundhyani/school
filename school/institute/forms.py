from django.contrib.auth.models import User
from django import forms
from .models import Institute
class SchoolRegistrationForm(forms.ModelForm):

    schoolname = forms.CharField(label = 'SchoolName', widget = forms.TextInput)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    phonenumber = forms.CharField(label='Phone Number',widget = forms.TextInput)
    phonenumber2 = forms.CharField(label = 'Additional Phone number',widget = forms.TextInput)
    email = forms.CharField(label = 'Backup email' , widget = forms.EmailInput)
    schooladdress = forms.CharField(label = 'Address of school' ,widget = forms.Textarea)
    class Meta:
        model = Institute 
        fields = ('name','phonenum')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']
