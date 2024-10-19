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
                  | MAIN_TITLE )

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
            print('--- это доктор')
            return True
        print('--- это не доктор')
        print([x['name'] for x in self.request.user.groups.values('name')])
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
            pacient_form = self.get_profile_form(requestion=request.POST) # при instace=None записывает новый
            if not pacient_form.is_valid():
                self.my_context['form_pacient'] = pacient_form
                return render(self.request, 'user_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            pacient = pacient_form.save(commit=False)
            pacient.user = self.get_user()
            pacient.save()
            return redirect('/weight_control/') # пациент профиль поправил успешно
        elif self.auth_as_doctor():
            doctor_form = self.get_profile_form(requestion=request.POST)
            if not doctor_form.is_valid():
                self.my_context['form_doctor'] = doctor_form
                return render(self.request, 'doctor_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            doctor = doctor_form.save(commit=False)
            doctor.user = self.get_user()
            doctor.save()
            doctor_form.save_m2m()
            return redirect('/weight_control/') # док профиль поправил успешно
        return redirect('/weight_control/') # если не зашел - регистрируйся


class Dashboard(My_View):
    def set_pacient_context(self):
        context = {}
        pacient_report_form = Pacient_Report_Form()
        context['form'] = pacient_report_form
        assign_ext = Assignment.objects.prefetch_related('preparats_list').filter(user_profile=self.get_profile())
        doc_prof_ext = Doctor_Profile.objects.prefetch_related('doc_specialty').all()
        context['assignments'] = [{'doctor': x.doctor_profile,
                                   'doc_specialty': [{'title': y.title, 'description': y.description}
                                                     for z in doc_prof_ext.filter(pk=x.doctor_profile.id)
                                                     for y in z.doc_specialty.all()],
                                   'description': x.description,
                                   'date': x.assign_date,
                                   'diet': x.diets,
                                   'preparats': [{'title': y.title, 'description': y.description}
                                                 for y in x.preparats_list.all()]}
                                  for x in assign_ext]
        return context
    def get(self, request):
        if self.auth_as_pacient():
            self.my_context = self.my_context | self.set_pacient_context()
            return render(self.request, 'dashboard_pacient.html', self.set_pacient_context() | MENU_DASHBOARD | MAIN_TITLE)
        return render(self.request, 'home_page.html', MENU | MAIN_TITLE)

    def post(self, request):
        pacient_report_form = Pacient_Report_Form(request.POST)
        if pacient_report_form.is_valid():
            report = pacient_report_form.save(commit=False)                                     #####
            report.pacient_profile = self.get_user_profile()                                    #####
            report.save()                                                                       #####
            pacient_report_form.save_m2m()                                                      #####
            return redirect('/weight_control/')
        self.my_context['form'] = pacient_report_form
        return render(self.request, 'home_page.html',self.my_context | MENU | MAIN_TITLE)



