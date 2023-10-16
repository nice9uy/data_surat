from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home' ),
     path('tambah_data/', views.tambah_data, name='tambah_data' ),
     path('setting/', views.setting, name='setting'),
     path('setting_tambah_data/', views.setting_tambah_data, name='setting_tambah_data'),
]