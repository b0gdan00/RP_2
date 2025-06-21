from arduino_connector import ArduinoSerial
from time import sleep
from .models import Sensor, Mechanism


arduino = ArduinoSerial()

def collect_data():
    
    co2_sensor = Sensor.objects.get(name="co2")
    light_sensor = Sensor.objects.get(name="light")
    temperature_sensor = Sensor.objects.get(name="temperature")
    
    while True:
        temperature = arduino.send_command("temp")
        temperature_sensor.value = temperature
        temperature_sensor.save()
        sleep(1)

        light = arduino.send_command("light")
                    # Конвертация: 68 (макс. свет) -> 100%, 800 (макс. темнота) -> 0%
        min_val, max_val = 68, 800
        percent = (max_val - float(light)) / (max_val - min_val) * 100
        percent = max(0, min(100, percent))  # Ограничить диапазон 0-100
        light_sensor.value = round(percent, 0)
        light_sensor.save()
        sleep(1)

        co2 = arduino.send_command("co2")
        co2_sensor.value = co2
        co2_sensor.save()
        sleep(1)
