from django.shortcuts import render
from arduino_connector import ArduinoSerial
from django.http import JsonResponse
from .models import Sensor, Mechanism

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

def index(request):

    context = {
        "name": "Control",
    }

    return render(request, 'index.html', context)
