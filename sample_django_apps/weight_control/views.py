from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import Pacient_Profile_Form, User_Creation_Form, Pacient_Report_Form, Assignment_Form, Doctor_profile_Form
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy
from .models import Pacient_Profile, Doctor_Profile, Pacient_reports, Assignment, Preparats_List, Specialty_List
from .config import MENU, MAIN_TITLE, MENU_DASHBOARD, MENU_ENTRANCE, MENU_REGISTRATION
import numpy as np
import matplotlib.pyplot as plt

# построение графиков

# график изменения веса

def plot_weight_graph(pacient_id):
    pacient_rep = Pacient_reports.objects.filter(pacient_profile_id=pacient_id).order_by('report_date')
    x = [a.report_date for a in pacient_rep]
    y = [a.weight_today for a in pacient_rep]
    # print(' -- строим ')
    # print(x,y)
    plt.figure(figsize=(6,4))
    plt.title('Динамика веса')
    plt.ylabel('Вес, кг')
    plt.grid()
    plt.ioff()
    plt.plot(x,y)
    plt.savefig('./static/media/graph_weight_1.png', transparent=True)


def plot_symptoms_graph(pacient_d):
    pass





# Create your views here.



def registration(request):
    if request.method == 'POST':
        form_user = User_Creation_Form(request.POST)
        form_pacient = Pacient_Profile_Form(request.POST)
        if form_user.is_valid() and form_pacient.is_valid():
            user_ = form_user.save()
            username = form_user.cleaned_data.get('username')
            password = form_user.cleaned_data.get('password1')
            pacient = form_pacient.save(commit=False)
            pacient.user = user_
            form_pacient.fields['registration_date'] = datetime.datetime.now()
            pacient.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/weight_control/')
    else:
        form_user = User_Creation_Form()
        form_pacient = Pacient_Profile_Form()

    return render(request, 'registration.html',
                  {'form_user': form_user}
                  | {'form_pacient': form_pacient}
                  | MENU_REGISTRATION
                  | MAIN_TITLE)


def home_page(request):
    return render(request, 'home_page.html', MENU | MAIN_TITLE)


def user_logout(request):
    logout(request)
    return redirect('/weight_control/')
    # return render(request,'home_page.html', MENU | MAIN_TITLE)


class User_logon(LoginView):
    form_class = AuthenticationForm
    template_name = 'logon.html'
    extra_context = MENU_ENTRANCE | MAIN_TITLE

    def get_success_url(self):
        return reverse_lazy('home_page')

def calculate_age(birth_date):
    if not birth_date:
        return 'не указан'
    else:
        today = datetime.date.today()
        return str(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))) + ' лет'


# расширим класс TemplateView - научим различать пользователей

class My_View(TemplateView):
    my_context = {}

    def user_is_auth(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_user(self, ):
        if self.user_is_auth():
            return User.objects.get(username=self.request.user)
        return None  # пользователь не вошел

    def get_user_groups(self):
        if not self.request.user.groups.values():
            return []  # пользователь вне групп
        return [x['name'] for x in self.request.user.groups.values('name')]  # возвращвем списки имен групп пользователя

    def auth_as_pacient(self):
        if self.user_is_auth() and len(self.get_user_groups()) == 0:
            return True
        return False

    def auth_as_doctor(self):
        if self.user_is_auth() and 'врач' in self.get_user_groups():
            return True
        return False

    def get_profile(self, ):
        if self.auth_as_doctor():
            if Doctor_Profile.objects.filter(user__username=self.request.user).exists():
                return Doctor_Profile.objects.get(user__username=self.request.user)
            else:
                return None
        elif self.auth_as_pacient():
            if Pacient_Profile.objects.filter(user__username=self.request.user).exists():
                return Pacient_Profile.objects.get(user__username=self.request.user)
            else:
                return None
        return None

    def get_profile_form(self, requestion=None):
        if self.auth_as_doctor():
            form = Doctor_profile_Form(requestion, instance=self.get_profile())
            return form
        elif self.auth_as_pacient():
            form = Pacient_Profile_Form(requestion, instance=self.get_profile())
            return form
        return None


class Profile_Edit(My_View):
    def get(self, request):
        if self.auth_as_pacient():
            pacient_form = self.get_profile_form()
            self.my_context['form_pacient'] = pacient_form
            return render(self.request, 'user_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        elif self.auth_as_doctor():
            doctor_form = self.get_profile_form()
            self.my_context['form_doctor'] = doctor_form
            return render(self.request, 'doctor_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        return render(self.request, 'home_page.html', MENU | MAIN_TITLE)

    def post(self, request):
        if self.auth_as_pacient():
            pacient_form = self.get_profile_form(requestion=request.POST)  # при instace=None записывает новый
            if not pacient_form.is_valid():
                self.my_context['form_pacient'] = pacient_form
                return render(self.request, 'user_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            pacient = pacient_form.save(commit=False)
            pacient.user = self.get_user()
            pacient.save()
            return redirect('/weight_control/')  # пациент профиль поправил успешно
        elif self.auth_as_doctor():
            doctor_form = self.get_profile_form(requestion=request.POST)
            if not doctor_form.is_valid():
                self.my_context['form_doctor'] = doctor_form
                return render(self.request, 'doctor_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            doctor = doctor_form.save(commit=False)
            doctor.user = self.get_user()
            doctor.save()
            doctor_form.save_m2m()
            return redirect('/weight_control/')  # док профиль поправил успешно
        return redirect('/weight_control/')  # если не зашел - регистрируйся


class Dashboard(My_View):
    def set_pacient_context(self):
        context = {}
        pacient_report_form = Pacient_Report_Form()
        context['form'] = pacient_report_form
        assign_ext = Assignment.objects.prefetch_related('preparats_list').filter(pacient_profile=self.get_profile())
        doc_prof_ext = Doctor_Profile.objects.prefetch_related('doc_specialty').all()
        context['assignments'] = [{'doctor': x.doctor_profile,
                                   'doc_specialty': [{'title': y.title, 'description': y.description}
                                                     for z in doc_prof_ext.filter(pk=x.doctor_profile.id)
                                                     for y in z.doc_specialty.all()],
                                   'description': x.description,
                                   'date': x.assign_date,
                                   'id': x.id,
                                   'diet': x.diets,
                                   'preparats': [{'title': y.title, 'description': y.description}
                                                 for y in x.preparats_list.all()]}
                                  for x in assign_ext]
        return context

    def set_doctor_context(self):
        context = {}
        pacient_id = self.request.GET.get('pacient_id')
        if not pacient_id:
            pacient_id = '0'
        assign_form = Assignment_Form()
        context['assign_form'] = assign_form
        pacient_list = Pacient_Profile.objects.filter(doc_attached=self.get_profile())
        context['pacient_list'] = [
            {'pacient': x, 'class': 'btn-select', 'id': x.id}
            if x.id == int(pacient_id)
            else {'pacient': x, 'class': 'btn-primary', 'id': x.id}
            for x in pacient_list]
        if pacient_id !='0':
            pacient_profile= Pacient_Profile.objects.get(id=int(pacient_id))
            context['pacient'] = pacient_profile
            context = context | {'age': calculate_age(pacient_profile.birth_date)}
            pacient_assign = Assignment.objects.prefetch_related('preparats_list', 'doctor_profile').filter(pacient_profile_id = int(pacient_id))
            context['pacient_assign'] = pacient_assign
            plot_weight_graph(int(pacient_id))
            plot_symptoms_graph(int(pacient_id))
        return context

    def get(self, request):
        if self.auth_as_pacient():
            self.my_context = self.my_context | self.set_pacient_context()
            return render(self.request, 'dashboard_pacient.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        elif self.auth_as_doctor():
            self.my_context = self.my_context | self.set_doctor_context()
            return render(self.request, 'dashboard_doctor.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        return render(self.request, 'home_page.html', MENU | MAIN_TITLE)

    def post(self, request):
        if self.auth_as_pacient():
            pacient_report_form = Pacient_Report_Form(request.POST)
            if pacient_report_form.is_valid():
                report = pacient_report_form.save(commit=False)  #####
                report.pacient_profile = self.get_profile()  #####
                report.save()  #####
                pacient_report_form.save_m2m()  #####
                return redirect('/weight_control/')
            self.my_context = self.set_pacient_context()
            self.my_context['form'] = pacient_report_form
            return render(self.request, 'dashboard_pacient.html', self.my_context | MENU | MAIN_TITLE)
        elif self.auth_as_doctor():
            pacient_id = self.request.GET.get('pacient_id')
            assign_form = Assignment_Form(self.request.POST)
            if assign_form.is_valid():
                print('валидно')
                assign = assign_form.save(commit=False)
                assign.pacient_profile = Pacient_Profile.objects.get(id = int(pacient_id))
                assign.doctor_profile = self.get_profile()
                print(assign)
                print(assign.pacient_profile.id)
                print(assign.doctor_profile.id)
                print(assign.diets)
                print(assign.description)
                assign.save()
                assign_form.save_m2m()
                return redirect('/weight_control/dashboard/')
            self.my_context = self.set_doctor_context()
            print('не валидно')
            print(assign_form.errors)
            self.my_context['assign_form'] = assign_form
            return render(self.request, 'dashboard_doctor.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        return redirect('/weight_control/')


