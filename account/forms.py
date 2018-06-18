from django import forms
from django.contrib.auth.models import User
from .models import Profile, Houses, trial

class LoginForm(forms.Form):    
    username = forms.CharField()    
    password = forms.CharField(widget=forms.PasswordInput) 


class UserRegistrationForm(forms.ModelForm):    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)    
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:        
        model = User        
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):        
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
            return cd['password2']

    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password', 'password2']:
            self.fields[fieldname].help_text = None
 
class UserEditForm(forms.ModelForm):    
    class Meta:        
        model = User        
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):    
    class Meta:        
        model = Profile 
        labels = {
            'City_of_residence': 'City of residence/Intended city of residence',
            'if_student': 'if you are a student, what institution are you in?'
        }       
        fields = ('__all__')

class HouseEditForm(forms.ModelForm):    
    class Meta:        
        model = Houses        
        fields = ('name_of_accomodation', 'type_of_room', 'house_rent', 'availability', 'location', 'nearest_institution', 'description', 'image') 

class TrialForm(forms.ModelForm):
    class Meta:
        model = trial
        fields = ('name', 'likes')

class ContactForm(forms.Form):
    Your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)