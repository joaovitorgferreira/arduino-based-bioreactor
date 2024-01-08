#define LED_1_PIN 9
#define LED_2_PIN 10
#define LED_3_PIN 11
#define LED_4_PIN 12

#define BUTTON_PIN 5

byte lastButtonState = LOW;
byte currentButtonState = LOW;
unsigned long lastButtonDebounceTime = 0;
unsigned long buttonDebounceDelay = 20;

void powerOffAllLEDs()
{
    digitalWrite(LED_1_PIN, LOW);
    digitalWrite(LED_2_PIN, LOW);
    digitalWrite(LED_3_PIN, LOW);
    digitalWrite(LED_4_PIN, LOW);
}

void setup()
{
  Serial.begin(9600);
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);
  pinMode(LED_3_PIN, OUTPUT);
  pinMode(LED_4_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);

  powerOffAllLEDs();
}

void loop()
{
  byte readValue = digitalRead(BUTTON_PIN);

  if (readValue != lastButtonState) {
    lastButtonDebounceTime = millis();
  }

  if (millis() - lastButtonDebounceTime > buttonDebounceDelay) {
    if (readValue != currentButtonState) {
      currentButtonState = readValue;
      if (currentButtonState == HIGH) {
        Serial.write(18);
      }
    }
  }

  lastButtonState = readValue;

  if (Serial.available() > 0) {
    int ledNumber = Serial.read() - '0';

    powerOffAllLEDs();
    
    switch (ledNumber) {
      case 1:
        digitalWrite(LED_1_PIN, HIGH);
        break;
      case 2:
        digitalWrite(LED_2_PIN, HIGH);
        break;
      case 3:
        digitalWrite(LED_3_PIN, HIGH);
        break;
      case 4:
        digitalWrite(LED_4_PIN, HIGH);
        break;
      default: 
        // wrong pin number, do nothing
        // all LEDs will be powered off
        break;
    }
  }
}
