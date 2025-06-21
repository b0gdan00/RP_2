import serial
import time
import sys

class ArduinoSerial:
    def __init__(self, port=None, baud_rate=9600, timeout=1):
        """Initialize the connection with Arduino, automatically detecting the port if not provided."""
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.port = port if port else self.find_arduino_port()

        if not self.port:
            self.ser = None
            raise ValueError("Arduino port not found!")

        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            time.sleep(2)  # Wait for serial initialization
            print(f"Connected to Arduino on {self.port}")
        except serial.SerialException as e:
            print(f"Failed to open serial port {self.port}: {e}")
            self.ser = None

    @staticmethod
    def find_arduino_port():
        """Automatically detect the Arduino port on Linux or Windows."""
        print(f"Detecting Arduino on {sys.platform}...")

        if sys.platform.startswith('linux'):
            return "/dev/ttyUSB0"
        elif sys.platform.startswith('win'):

            return "COM4" 
        else:
            return None  # Unsupported system

    def send_command(self, command):
        """Отправляет команду и ждёт один ответ"""
        if not self.ser:
            print("Serial connection not established.")
            return None
        self.ser.write((command + '\n').encode())  # Отправка
        response = self.ser.readline().decode().strip()  # Чтение ответа
        return response
            

    def close(self):
        """Закрывает соединение"""
        if self.ser:
            self.ser.close()
