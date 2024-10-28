from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import Pacient_Profile_Form, User_Creation_Form, Pacient_Report_Form, Assignment_Form, Doctor_profile_Form
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy
from .models import Pacient_Profile, Doctor_Profile, Pacient_reports, Assignment
from .config import MENU, MAIN_TITLE, MENU_DASHBOARD, MENU_ENTRANCE, MENU_REGISTRATION, MENU_MANAGER_REG, WELCOME
import matplotlib.pyplot as plt


# построение графиков

# график изменения веса

def plot_weight_graph(pacient_id):
    """
    строит график изменения веса пациента
    и сохраняет его в файл
    :param pacient_id: ссылка на профиль пациента
    :return: ничего не возвращает
    """
    pacient_rep = Pacient_reports.objects.filter(pacient_profile_id=pacient_id).order_by('report_date')
    x = [a.report_date for a in pacient_rep]  # дата отчета
    y = [a.weight_today for a in pacient_rep]  # вес в этом отчете
    plt.figure(figsize=(6, 4))
    plt.title('Динамика веса')
    plt.ylabel('Вес, кг')
    plt.xlabel('Время')
    plt.grid()
    plt.ioff()
    plt.plot(x, y)
    plt.savefig(f'./static/media/graph_weight_{pacient_id}.png', transparent=True)


# строим график частоты появления симптомов
def plot_symptoms_graph(pacient_id):
    """
    строит график частоты симптомов
    проявляющихся у пациента
    :param pacient_id: ссылка на профиль пациента
    :return: ничего не возвращает
    """
    pacient_symp = Pacient_reports.objects.prefetch_related('symptoms_list').filter(pacient_profile_id=pacient_id)
    symp = [y.title for x in pacient_symp for y in x.symptoms_list.all()]  # все вхождения симптомов
    x = list(set(symp))  # имена симптомов
    y = [symp.count(z) for z in x]  # подсчитываем каждый симптом сколько раз появился
    plt.figure(figsize=(6, 4))
    plt.title('Наблюдаемые симптомы')
    plt.ylabel('Частота появления')
    plt.xlabel('Симптом')
    plt.grid()
    plt.ioff()
    plt.bar(x, y)
    plt.savefig(f'./static/media/graph_symptom_{pacient_id}.png', transparent=True)
    pass


# Create your views here.

def home_page(request):
    """
    Представление домашней страницы
    :param request: HTTP запрос
    :return: отправляет HTML домашней страницы
    """
    return render(request, 'home_page.html', WELCOME | MENU | MAIN_TITLE)


def registration(request):
    """
    Представление страницы регистрации пациента
    :param request: HTTP запрос
    :return: отправляет HTML страницы регистрации,
    а если пользователь успешно зарегистрировался - редирект в личный кабинет
    """
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
            return redirect('/weight_control/dashboard/')
    else:
        form_user = User_Creation_Form()
        form_pacient = Pacient_Profile_Form()

    return render(request, 'registration.html',
                  {'form_user': form_user}
                  | {'form_pacient': form_pacient}
                  | MENU_REGISTRATION
                  | MAIN_TITLE)


def user_logout(request):
    """
    осуществляет выход пользователя из системы
    :param request: входящий запрос
    :return: редирект на главную страницу
    """
    logout(request)
    return redirect('/weight_control/')
    # return render(request,'home_page.html', MENU | MAIN_TITLE)


class User_logon(LoginView):
    """
    Представление страницы входа пользователя
    """
    form_class = AuthenticationForm
    template_name = 'logon.html'
    extra_context = MENU_ENTRANCE | MAIN_TITLE

    def get_success_url(self):
        """
        успешнфй вход в систему
        :return: редирект в личный кабинет
        """
        return reverse_lazy('dashboard')


def calculate_age(birth_date):
    """
    вычисляет возраст на текущий момент
    :param birth_date: дата рождения
    :return: строку возраста в годах или 'не указан', если дата рождения 'пустая'
    """
    if not birth_date:
        return 'не указан'
    else:
        today = datetime.date.today()
        return str(
            today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))) + ' лет'


# расширим класс TemplateView - научим различать пользователей

class My_View(TemplateView):
    """
    дополнение стандартного класса новыми методами, для дальнейшего использования в представлениях
    """
    my_context = {}

    def user_is_auth(self):
        """
        проверяет вошел ли пользователь в систему
        :return: Истина если вошел, Ложь если не вошел
        """
        if self.request.user.is_authenticated:
            return True
        return False

    def get_user(self, ):
        """
        получает объект пользователя из БД
        :return: возвращает объект пользователя или Пусто если пользователь не вошел в систему
        """
        if self.user_is_auth():
            return User.objects.get(username=self.request.user)
        return None  # пользователь не вошел

    def get_user_groups(self):
        """
        возвращает список групп в которые входит пользователь
        :return: список групп
        """
        if not self.request.user.groups.values():
            return []  # пользователь вне групп
        return [x['name'] for x in self.request.user.groups.values('name')]  # возвращвем списки имен групп пользователя

    def auth_as_pacient(self):
        """
        определяет авторизован ли пользователь как пациент
        :return: Истина если пациент, Ложь если не пациент
        """
        if self.user_is_auth() and len(self.get_user_groups()) == 0:
            return True
        return False

    def auth_as_doctor(self):
        """
        определяет авторизован ли пользователь как врач
        :return: Истина если врач, Ложь если не врач
        """
        if self.user_is_auth() and 'врач' in self.get_user_groups():
            return True
        return False

    def auth_as_manager(self):
        """
        определяет авторизован ли пользователь как менеджер
        :return: Истина если менеджер, Ложь если не менеджер
        """
        if self.user_is_auth() and 'менеджер' in self.get_user_groups():
            return True
        return False

    def get_profile(self, ):
        """
        получает объект профиля пользователя из БД
        :return: объект профиля пользователя или пусто если профиля нет
        """
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
        """
        получает форму профиля пользователя, заполняет её данными из запроса
        :param requestion: запрос
        :return: форма профиля пользователя, или Пусто если формы не существует
        """
        if self.auth_as_doctor():
            form = Doctor_profile_Form(requestion, instance=self.get_profile())
            return form
        elif self.auth_as_pacient():
            form = Pacient_Profile_Form(requestion, instance=self.get_profile())
            return form
        return None


class Profile_Edit(My_View):
    """
    представление страницы редактирования/создания профиля
    """

    def get(self, request):
        """
        формирует страницу редактирования профиля
        :param request: входящий запрос
        :return: страницу редактирования профиля или главную страницу если пользователь не авторизован
        """
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
        """
        сохраняет измененнй/новый профиль
        :param request:
        :return: редирект в личный кабинет
        """
        if self.auth_as_pacient():
            pacient_form = self.get_profile_form(
                requestion=request.POST)  # при instace=None записывает новый (если профиля еще нет)
            if not pacient_form.is_valid():
                self.my_context['form_pacient'] = pacient_form
                return render(self.request, 'user_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            pacient = pacient_form.save(commit=False)
            pacient.user = self.get_user()
            pacient.save()
            return redirect('/weight_control/dashboard/')  # пациент профиль поправил успешно
        elif self.auth_as_doctor():
            doctor_form = self.get_profile_form(requestion=request.POST)
            if not doctor_form.is_valid():
                self.my_context['form_doctor'] = doctor_form
                return render(self.request, 'doctor_profile_edit.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            doctor = doctor_form.save(commit=False)
            doctor.user = self.get_user()
            doctor.save()
            doctor_form.save_m2m()
            return redirect('//weight_control/dashboard/')  # док профиль поправил успешно
        return redirect('/weight_control/')  # если не зашел - регистрируйся


class Dashboard(My_View):
    """
    представление личного кабинета пользователя
    """

    def set_pacient_context(self):
        """
        создает контекст кабинета пациента
        :return: контекст кабинета пациента
        """
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
        """
        создает контекст кабинета врача
        :return: контекст кабинета врача
        """
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
        if pacient_id != '0':
            pacient_profile = Pacient_Profile.objects.get(id=int(pacient_id))
            context['pacient'] = pacient_profile
            context = context | {'age': calculate_age(pacient_profile.birth_date)}
            pacient_assign = Assignment.objects.prefetch_related('preparats_list', 'doctor_profile').filter(
                pacient_profile_id=int(pacient_id))
            context['pacient_assign'] = pacient_assign
            plot_weight_graph(int(pacient_id))
            plot_symptoms_graph(int(pacient_id))
        return context

    def get(self, request):
        """
        создает личный кабинет
        :param request: входящий запрос
        :return: страница личного кабинета или главная страница, если пользователь не авторизован
        """
        if self.auth_as_pacient():
            self.my_context = self.my_context | self.set_pacient_context()
            return render(self.request, 'dashboard_pacient.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        elif self.auth_as_doctor():
            self.my_context = self.my_context | self.set_doctor_context()
            return render(self.request, 'dashboard_doctor.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        elif self.auth_as_manager():
            return render(self.request, 'dashboard_manager.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE | MENU_MANAGER_REG)
        return redirect('/weight_control/')


    def post(self, request):
        """
        сохраняет результат работы пользователя в личном кабинете в базу данных
        :param request: входящий запрос
        :return: страница личного кабинета
        """
        if self.auth_as_pacient():
            pacient_report_form = Pacient_Report_Form(request.POST)
            if pacient_report_form.is_valid():
                report = pacient_report_form.save(commit=False)
                report.pacient_profile = self.get_profile()
                report.save()
                pacient_report_form.save_m2m()
                # тут уведомим об успешной отправке и задисейблим кнопку
                self.my_context = self.set_pacient_context()
                self.my_context['disabled'] = 'disabled'
                return render(self.request, 'dashboard_pacient.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
            self.my_context = self.set_pacient_context()
            self.my_context['form'] = pacient_report_form
            return render(self.request, 'dashboard_pacient.html', self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        elif self.auth_as_doctor():
            pacient_id = self.request.GET.get('pacient_id')
            assign_form = Assignment_Form(self.request.POST)
            if assign_form.is_valid():
                assign = assign_form.save(commit=False)
                assign.pacient_profile = Pacient_Profile.objects.get(id=int(pacient_id))
                assign.doctor_profile = self.get_profile()
                assign.save()
                assign_form.save_m2m()
                return redirect('/weight_control/dashboard/')
            self.my_context = self.set_doctor_context()
            self.my_context['assign_form'] = assign_form
            return render(self.request, 'dashboard_doctor.html',
                          self.my_context | MENU_DASHBOARD | MAIN_TITLE)
        return redirect('/weight_control/dashboard/')
