from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('ruangan', views.ruangan, name='ruangan'),
    path('alat', views.alat, name='alat'),
    path('paduan', views.paduan, name='paduan'),
    path('labkomputer', views.borangkomputer, name='borangkomputer'),
    path('gorlapangan', views.gor, name='borang-gor-lapangan'),
    path('auditorium', views.auditorium, name='borang-auditorium'),
    path('labkimia', views.labkimia, name='borang-kimia'),
    path('laptop', views.laptop, name='borang-laptop'),
    path('kamera', views.kamera, name='borang-kamera'),
    path('drone', views.drone, name='borang-drone'),
    path('ipad', views.ipad, name='borang-ipad'),
]