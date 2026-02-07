const int greenLED = 6;
const int redLED = 7;
const int buzzer = 8;
void setup()
{
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, LOW);
  noTone(buzzer);

  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    char command = Serial.read();

    if (command == 'A')
    {
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, HIGH);
      tone(buzzer, 1000);  // Play 1kHz tone
    } 
    else if (command == 'R')
    {
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
      noTone(buzzer);
    }
  }
}
