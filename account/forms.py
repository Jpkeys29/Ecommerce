from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #To validate email(unique email)
    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)

    #Mark email field as required:
        self.fields['email'].required = True
    

    #Email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is invalid')
        if len(email) >=200:
            raise forms.ValidationError('Your email is too long')
        
        return email   #so that the email gets save in the db

#Login form
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)

#Update form

class UpdateUserForm(forms.ModelForm):
    password = None  #password does not need to be updated
    class Meta:
        model = User

        fields = ['username','email']
        exclude = ['password1', 'password1']

    #To validate email(unique email)
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm,self).__init__(*args, **kwargs)

    #Mark email field as required:
        self.fields['email'].required = True


