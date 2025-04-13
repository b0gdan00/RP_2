from django.shortcuts import render
from arduino_connector import ArduinoSerial
from django.http import JsonResponse
from .models import Sensor, Mechanism
from django.views.decorators.csrf import csrf_exempt
import json

arduino = ArduinoSerial()

def get_temperature(request):
    if request.method == 'GET':
        try:
            sensor = Sensor.objects.get(name="temperature")
            temp = arduino.send_command("temp")  # или нужная тебе команда
            sensor.value = temp
            sensor.save()
            return JsonResponse({'temperature': temp})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_humidity(request):
    if request.method == 'GET':
        try:
            sensor = Sensor.objects.get(name="hiumidity")
            humidity = arduino.send_command("humidity")  # или нужная тебе команда
            sensor.value = humidity
            sensor.save()
            return JsonResponse({'humidity': humidity})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_light(request):
    if request.method == 'GET':
        try:
            sensor = Sensor.objects.get(name="light")
            light = arduino.send_command("light")  # или нужная тебе команда
            sensor.value = light
            sensor.save()
            return JsonResponse({'light': light})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_planty(request):
    if request.method == 'GET':
        try:
            planty = 43
            return JsonResponse({'planty': planty})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def update_heater_value(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            heater_value = data.get('heater_value')

            # Update the heater value in the database
            heater = Mechanism.objects.get(name="heater")
            heater.normal_value = heater_value
            heater.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def index(request):

    heater = Mechanism.objects.get(name="heater")

    context = {
        "name": "Control",
        "heater": heater,
    }

    return render(request, 'index.html', context)
