from django import forms


class LoginUserForm(forms.Form):
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
