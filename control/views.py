from django.shortcuts import render
from arduino_connector import ArduinoSerial
from django.http import JsonResponse
from .models import Sensor, Mechanism
from django.views.decorators.csrf import csrf_exempt
import json


arduino = ArduinoSerial()


def index(request):

    heater = Mechanism.objects.get(name="heater")
    light = Mechanism.objects.get(name="light")
    co2 = Mechanism.objects.get(name="co2")
    pump = Mechanism.objects.get(name="pump")


    context = {
        "name": "Control",
        "heater": heater,
        "light": light,
        "co2": co2,
        "pump": pump,

    }

    return render(request, 'index.html', context)


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
            humidity = arduino.send_command(
                "humidity")  # или нужная тебе команда
            sensor.value = humidity
            sensor.save()
            return JsonResponse({'humidity': humidity})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def get_light(request):
    if request.method == 'GET':
        try:
            sensor = Sensor.objects.get(name="light")
            raw_light = arduino.send_command("light")  # или нужная тебе команда

            # Конвертация: 68 (макс. свет) -> 100%, 800 (макс. темнота) -> 0%
            min_val, max_val = 68, 800
            percent = (max_val - float(raw_light)) / (max_val - min_val) * 100
            percent = max(0, min(100, percent))  # Ограничить диапазон 0-100

            sensor.value = round(percent,0)
            sensor.save()
            return JsonResponse({'light': percent})
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
def update_heater(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            heater_value = data.get('value')
            heater_status = data.get('status')

            # Update the heater value in the database
            heater = Mechanism.objects.get(name="heater")
            heater.status = heater_status
            heater.normal_value = heater_value
            if heater_status == False: heater.off()
            else: heater.on()
            heater.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def update_light(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            status = data.get('status')

            # Update the heater value in the database
            light = Mechanism.objects.get(name="light")
            light.status = status
            light.normal_value = value
            if status == False: light.off()
            else: light.on()
            light.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def update_co2(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            status = data.get('status')

            # Update the heater value in the database
            co2 = Mechanism.objects.get(name="co2")
            co2.status = status
            co2.normal_value = value
            if status == False: co2.off()
            else: co2.on()
            co2.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def update_pump(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            status = data.get('status')

            # Update the heater value in the database
            pump = Mechanism.objects.get(name="pump")
            pump.status = status
            pump.normal_value = value
            pump.period = data.get('period')
            if status == False: pump.off()
            else: pump.on()
            pump.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
