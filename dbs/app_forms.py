from django import forms

from dbs.models import Customer

GENDER_CHOICES = {"Male": "Male", "Female": "Female"}

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'dob', 'weight', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type':'date','min':'1990-01-01', 'max':'2013-12-31'}),
            'weight': forms.TextInput(attrs={'type':'number','min':'0','max':'100'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
