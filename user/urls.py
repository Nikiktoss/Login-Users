from django.urls import path
from .views import *

urlpatterns = [
    path('', sign_in_user, name="login_page"),
    path('main', index, name='main_page'),
    path('exit', logout_from_app, name="logout"),
    path('sign_up', registrate_user, name="registration_page"),
]
