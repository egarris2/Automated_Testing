//recieves commands from serial and prints them back
/*
#include "Arduino.h"
int led1 = 22;
int led2 = 24;
int led3 = 26;
int x;
void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  Serial.begin(19200);
  Serial.flush();
}

void loop() {
  String input;
  String inputln;

  Serial.println("Waiting for input:");
  while (input != "\n")
  {
    if (Serial.available() > 0)
    {
          input = (char) Serial.read();
          inputln += input;
    }
  }
  Serial.print("recieved input:");
  Serial.print(inputln);

  if (inputln == "1 on\n")
  {
    digitalWrite(led1, HIGH);
  }
  else if (inputln == "1 off\n")
  {
    digitalWrite(led1, LOW);
  }

  if (inputln == "2 on\n")
  {
    digitalWrite(led2, HIGH);
  }
  else if (inputln == "2 off\n")
  {
    digitalWrite(led2, LOW);
  }

  if (inputln == "3 on\n")
  {
    digitalWrite(led3, HIGH);
  }
  else if (inputln == "3 off\n")
  {
    digitalWrite(led3, LOW);
  }

  if (inputln == "all on\n")
  {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
  }
  else if (inputln == "all off\n")
  {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }

  if (inputln == "rave\n")
  {
    for (x = 0; x<20; x++)
    {
    digitalWrite(led1, HIGH);
    delay(40);
    digitalWrite(led3, LOW);
    delay(40);
    digitalWrite(led2, HIGH);
    delay(40);
    digitalWrite(led1, LOW);
    delay(40);
    digitalWrite(led3, HIGH);
    delay(40);
    digitalWrite(led2, LOW);
    }
    digitalWrite(led3, LOW);
  }
}
*/
