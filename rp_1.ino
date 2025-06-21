#include <Adafruit_AHTX0.h>


#define DHTPIN 2
#define LIGHT_IN A0
#define CO2_IN A1

Adafruit_AHTX0 aht;

const int LED_PIN = 13;  // Встроенный светодиод
const int LIGHT_OUT = 8;
const int CO2_OUT = 9;
const int TEN = 11;
const int PUMP = 12;


void setup() {

  pinMode(LED_PIN, OUTPUT);

  pinMode(LIGHT_OUT, OUTPUT);
  pinMode(CO2_OUT, OUTPUT);
  pinMode(TEN, OUTPUT);
  pinMode(PUMP, OUTPUT);



  // digitalWrite(LIGHT_OUT, HIGH);
  // digitalWrite(CO2_OUT, HIGH);
  // digitalWrite(TEN, HIGH);
  // digitalWrite(PUMP, HIGH);
  aht.begin();
  // pinMode(LIGHT_IN, INPUT);



  Serial.begin(9600);
}

void loop() {


  sensors_event_t humidity, temp;

  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ping") {
      Serial.println("pong");
    } else if (command == "temp") {
      aht.getEvent(&humidity, &temp);
      Serial.println(temp.temperature);
    } else if (command == "humidity") {
      aht.getEvent(&humidity, &temp);
      Serial.println(humidity.relative_humidity);
    } else if (command == "light") {
      int light = analogRead(LIGHT_IN);
      Serial.println(light);
    } else if (command == "co2") {
      int co2 = analogRead(CO2_IN);
      Serial.println(co2);


    } else if (command == "co2 on") {
      digitalWrite(CO2_OUT, HIGH);
    } else if (command == "co2 off") {
      digitalWrite(CO2_OUT, LOW);
    } else if (command == "temp on") {
      digitalWrite(TEN, HIGH);
    } else if (command == "temp off") {
      digitalWrite(TEN, LOW);
    } else if (command == "light on") {
      digitalWrite(LIGHT_OUT, HIGH);
    } else if (command == "light off") {
      digitalWrite(LIGHT_OUT, LOW);
    } else if (command == "pump on") {
      digitalWrite(PUMP, HIGH);
    } else if (command == "pump off") {
      digitalWrite(PUMP, LOW);
    } else {
      Serial.println("Unknown command");
    }
  }



  // aht.getEvent(&humidity, &temp);
  // int light = analogRead(LIGHT_IN);
  // int co2 = analogRead(CO2_IN);

  // Serial.print("Temperature: ");
  // Serial.print(temp.temperature);
  // Serial.println(" C");

  // Serial.print("Humidity: ");
  // Serial.print(humidity.relative_humidity);
  // Serial.println(" %");

  // Serial.print("Light: ");
  // Serial.println(light);

  // Serial.print("CO2: ");
  // Serial.println(co2);

  // Serial.println("----------------------");

  // delay(1000); // щоб не спамило кожну мілісекунду
}
