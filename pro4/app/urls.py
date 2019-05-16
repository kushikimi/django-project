from django.urls import path
from . import views

app_name='app'

urlpatterns=[path('',views.user_login,name='user_login'),
path('register/',views.Reg,name='register'),
path('logout/',views.user_logout,name='logout')


]
