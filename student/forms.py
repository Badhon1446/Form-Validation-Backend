from . import models
from django import forms


class StudentForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = models.Student
        fields = '__all__'
        lables = {
            'name' : "Full Name",
            'email' : "Email address",
            'phone' : "Phone number",
            'photo' : "Upload File",
        }
        help_texts = {
            'email': "Don't share your email",
            'password': "Password is your secqurity.",
        }

       