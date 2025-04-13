from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('api/temperature/', get_temperature, name='get_temperature'),
    path("api/humidity/", get_humidity, name="get_humidity"),
    path("api/light/", get_light, name="get_light"),
    path("api/planty/", get_planty, name="get_planty"),
    path('update_heater_value/', update_heater_value, name='update_heater_value'),
]
