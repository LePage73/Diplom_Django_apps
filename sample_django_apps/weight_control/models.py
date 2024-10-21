from django.db import models
from django.contrib.auth.models import User
from .config import CHOICE_GENDER
from datetime import date

# Create your models here.

class Specialty_List(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title
class Doctor_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    family = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    doc_stage = models.IntegerField()
    self_description = models.TextField(unique=False, default="Ничего не известно")
    doc_specialty = models.ManyToManyField(Specialty_List)
    registration_date = models.DateField(null=False, blank=True, default=date.today)
    adress = models.CharField(max_length=100, unique=False, default="Адрес не указан")
    foto_file_path = models.CharField(max_length=120, unique=False, blank=True)
    gender = models.CharField(choices=CHOICE_GENDER, max_length=7, blank=False, default=1)

    def calculate_age(self, birth_date):
        if not birth_date:
            return 'не указан'
        else:
            today = date.today()
            return (str(today.year -
                        birth_date.year +
                        ((today.month, today.day) < (birth_date.month, birth_date.day))) + ' лет')


    def __str__(self):
        return (self.family + ' ' +
                self.first_name + ' ' +
                self.second_name + ', ' +
                self.calculate_age(self.birth_date))

class Pacient_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    family = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=100, unique=False, default="Адрес не указан")
    birth_date = models.DateField(null=True, blank=True)
    first_diagnos = models.TextField(unique=False)
    start_weight = models.DecimalField(max_digits=6, decimal_places=3, )
    gender = models.CharField(choices=CHOICE_GENDER, max_length=7, blank=False)
    registration_date = models.DateField(null=False, blank=False, default=date.today)
    email = models.CharField(max_length=50, blank=True, unique=False)
    doc_attached = models.ForeignKey(Doctor_Profile, on_delete=models.PROTECT, default=None, unique=False, blank=True, null=True)

    def calculate_age(self, birth_date):
        if  not birth_date:
            return 'не указан'
        else:
            today = date.today()
            return str(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))) + ' лет'

    def __str__(self):
        return self.family + ' ' + self.first_name + ' ' + self.second_name + ', ' + self.calculate_age(self.birth_date)








class Diets_List(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(unique=False)
    foto_file_path = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Preparats_List(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(unique=False)
    foto_file_path = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    assign_date = models.DateField(null=False, blank=True, default=date.today)
    pacient_profile = models.ForeignKey(Pacient_Profile, on_delete=models.PROTECT,unique=False,null=True)
    doctor_profile = models.ForeignKey(Doctor_Profile, on_delete=models.PROTECT, unique=False,null=True)
    diets = models.ForeignKey(Diets_List, on_delete=models.PROTECT, unique=False)
    preparats_list = models.ManyToManyField(Preparats_List, unique=False)
    description = models.TextField(unique=False)

class Symptoms_list(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Pacient_reports(models.Model):
    report_date = models.DateField(null=False, blank=True, default=date.today, unique=False)
    pacient_profile = models.ForeignKey(Pacient_Profile, on_delete=models.CASCADE, unique=False)
    weight_today = models.DecimalField(max_digits=6, decimal_places=3, unique=False)
    symptoms_list = models.ManyToManyField(Symptoms_list, unique=False)
    description = models.TextField(unique=False, null=True)

class Diseases_List(models.Model):
    title = models.CharField(max_length=50)
    diseases_description = models.TextField()

class Accompanying_disease_pacients(models.Model):
    disease_list_id = models.ManyToManyField(Diseases_List)

class Doc_ratings(models.Model):
    doctor_profile = models.OneToOneField(Doctor_Profile, on_delete=models.PROTECT)
    pacient_profile = models.OneToOneField(Pacient_Profile, on_delete=models.PROTECT)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1,)



