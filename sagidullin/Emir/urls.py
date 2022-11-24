from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fio', views.fio),
    path('about', views.about),
    path('contacts', views.contacts),
]