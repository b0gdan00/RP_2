from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('api/temperature/', get_temperature, name='get_temperature'),
    path("api/co2/", get_co2, name="get_co2"),
    path("api/light/", get_light, name="get_light"),
    path("api/planty/", get_planty, name="get_planty"),
    path('update_heater/', update_heater, name='update_heater'),
    path('update_light/', update_light, name='update_light'),
    path('update_co2/', update_co2, name='update_co2'),
    path('update_pump/', update_pump, name='update_pump'),
    
]
