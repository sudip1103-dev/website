#django imports
from django import forms
from django.contrib.auth.models import User

#class import
import machine_usage.lists
from machine_usage.models import UserProfile

class ForgeUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ForgeProfileCreationForm(forms.ModelForm):
    rin = forms.CharField()
    gender = forms.Select(choices=machine_usage.lists.gender)
    major = forms.Select(choices=machine_usage.lists.major)
    

    class Meta:
        model = UserProfile 
        fields = ('rin','gender','major')

    def is_valid(self):
        valid = super(ForgeProfileCreationForm, self).is_valid()
        rin = self.cleaned_data.get("rin")
        
        if(len(rin)!=9):
            valid = False
            self._errors['rin_error'] = 'Invalid rin'
        try:
            rin = int(rin)
        except:
            valid = False
            self._errors['rin_error'] = 'Invalid rin'
        
        
        if not valid:
            return False
        
        return  True
        
