from django import forms 

from .models import User


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        
        fields = ['phone', 'email', 'username', 'password', 'first_name', 'last_name']
        
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control my-5', 'placeholder':'example1234@gmail.com'}),
            'phone': forms.NumberInput(attrs={'class':'form-control my-5', 'placeholder':'09123456789'}),
            'username': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}),
            'first_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'John'}),
            'last_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Doe'}),
        }


class OTPForm(forms.Form):
    otp = forms.CharField(label="OTP", max_length=6)


class UserUpdate(forms.Form):
    phone      = forms.CharField(label="Phone Number")
    email      = forms.EmailField(label="Email")
    username   = forms.CharField(label="Username")
    first_name = forms.CharField(label="Name")
    last_name  = forms.CharField(label="Family Name")
    
    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control my-3'})
