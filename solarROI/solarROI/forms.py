from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
'''
class CustomRegistrationFormTest(UserCreationForm):
    def __init__(self):
        self.fields = (
            forms.EmailField(required=True),
        )
    
    def isValidUsername(self, field_data, all_data):
        try:
            User.objects.get(username=field_data)
        except User.DoesNotExist:
            return
        raise validators.ValidationError('The username "%s" is already taken.' % field_data)
    
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],
                                     new_data['email'],
                                     new_data['password1'])
        u.is_active = False
        u.save()
        return u
'''

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,\
    widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name',\
                  'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def save(self, commit=True):        
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()

        return user
