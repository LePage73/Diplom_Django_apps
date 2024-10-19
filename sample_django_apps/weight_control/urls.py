from django.urls import path, include
from .views import registration, home_page, user_logout, User_logon, Profile_Edit, Dashboard

urlpatterns = [
    path('', home_page),
    path('weight_control/registration/', registration, name='registration'),
    path('weight_control/', home_page,name='home_page'),
    path('weight_control/logout/', user_logout, name='logout'),
    path('weight_control/entrance/',User_logon.as_view(), name='logon'),
    path('weight_control/dashboard/profile/', Profile_Edit.as_view(), name='edit_profile'),
    path('weight_control/dashboard/', Dashboard.as_view(), name='dashboard'),
]

