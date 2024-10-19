import datetime
from django.forms import NumberInput
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Pacient_Profile, Doctor_Profile, Pacient_reports, Symptoms_list, Assignment
from .config import CHOICE_GENDER

class Pacient_Profile_Form(ModelForm):
    gender = forms.ChoiceField(choices=CHOICE_GENDER, )
    email = forms.EmailField(initial='vash_email@domen.ru', required=False)
    registration_date = forms.DateField(required=False)

    class Meta:
        model = Pacient_Profile
        exclude = ['user']
        # fields = '__all__'
        widgets = {'family': forms.TextInput(attrs={'placeholder': 'Фамилия', 'autofocus': 'true'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'Имя', }),
                   'second_name': forms.TextInput(attrs={'placeholder': 'Отчество', }),
                   'phone_number': forms.TextInput(attrs={'placeholder': '+7(9XX)-XXX-XX-XX', }),
                   'adress': forms.Textarea(attrs={'cols': '100%', 'rows': 2,
                                                   'placeholder': 'Адрес: \nМосква, 3-я улица Строителей, д.5, кв. 12', }),
                   'birth_date': NumberInput(attrs={'type': 'date', }),
                   'first_diagnos': forms.Textarea(attrs={'cols': '100%', 'rows': 5, 'placeholder': 'Диагноз', }),
                   'start_weight': NumberInput(attrs={'type': 'number', 'placeholder': 'Ваш вес, кг', }),
                   'gender': forms.RadioSelect(attrs={}, ),
                   'email': forms.TextInput(attrs={'placeholder': 'vash_email@domen.ru', }),

                   }

class User_Creation_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Ваш логин'}),
                   'password1': forms.PasswordInput(attrs={}),
                   'password2': forms.PasswordInput(attrs={}),
                   }

class User_logon_Form(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Ваш логин'}),
                   'password': forms.PasswordInput(attrs={}),
                   }

class Doctor_profile_Form(ModelForm):
    class Meta:
        model = Doctor_Profile
        fields = '__all__'
        widgets = {'family': forms.TextInput(attrs={'placeholder': 'Фамилия', 'autofocus': 'true'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'Имя', }),
                   'second_name': forms.TextInput(attrs={'placeholder': 'Отчество', }),
                   'phone_number': forms.TextInput(attrs={'placeholder': '+7(9XX)-XXX-XX-XX', }),
                   'adress': forms.Textarea(attrs={'cols': '100%', 'rows': 2,
                                                   'placeholder': 'Адрес: \nМосква, 3-я улица Строителей, д.5, кв. 12', }),
                   'birth_date': NumberInput(attrs={'type': 'date', }),
                   }


class Dashboard_Form(forms.Form):

    pass

class Pacient_Report_Form(ModelForm):
    OPTION = [(x.id, x.title) for x in Symptoms_list.objects.all()]
    symptoms_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTION)

    class Meta:
        model = Pacient_reports
        exclude = ['pacient_profile']
        widgets = {'weight_today': NumberInput(attrs={'type': 'number', 'placeholder': 'Ваш вес сегодня, кг', }),
                   'description': forms.Textarea(attrs={ 'cols': 28, 'rows': 2, 'placeholder': 'Опишите кратко свое состояние', }),
                   }

class Assignment_Form(ModelForm):
    # preparats_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Assignment
        exclude = ['assign_date']
        # fields = '__all__'
