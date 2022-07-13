from .models import Game
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea,forms, DateTimeField,DateInput,DateField
from django.contrib.auth.models import User

class DateInput(DateInput):
    input_type='date'

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = [ 'name', 'task','date']

        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Имя события'
            }),
        "task": Textarea(attrs={
            'class' : 'form-control',
            'placeholder':'Описание события'
            }),
        "date": DateInput #(attrs={
            #'class' : 'form-control'
            #})
        }
# class GameForm(forms.Form):
#     name = forms.CharField('Имя события', max_length=50)
#     task = forms.TextField('Описание события')
#     date = forms.DateField('Дата события')


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']