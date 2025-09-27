
from django.contrib import admin
from django.urls import path
from tomapp.views import bmi_calculator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bmi_calculator, name='bmi_calculator'),
]

