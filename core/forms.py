from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-input'
            })

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['job_role', 'experience_years', 'resume']
        widgets = {
            'job_role': forms.TextInput(attrs={
                'placeholder': 'e.g., Full Stack Developer, Data Scientist',
            }),
            'experience_years': forms.NumberInput(attrs={
                'min': '0',
                'max': '50',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # Add CSS classes to form fields
        for field_name in self.fields:
            if field_name != 'resume':
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-input'
                })
