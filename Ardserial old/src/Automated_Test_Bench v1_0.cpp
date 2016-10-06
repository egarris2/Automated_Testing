//Automated test bench v1.0
//Control an Arduino MEGA using seral commands
//date: 8/16/16
#include "Arduino.h"

int dpin22 = 22;
int dpin24 = 24;
int dpin26 = 26;
int dpin28 = 28;
String inputln;
int integer;

void serialCom();
void pinSet();
void pinVal22();
void pinVal24();
void pinVal26();
void readSensor();

void setup()
{
  Serial.begin(115200);
  Serial.flush();
  Serial.print("Automated Test Bench v1.0\n");
}

void loop()
{
  Serial.flush();
  serialCom();
  pinSet();
  pinVal22();
  pinVal24();
  pinVal26();
  readSensor();
  inputln = "";
}



void serialCom()
{
  String input;

  while (input != "\n")
  {
    if (Serial.available() > 0)
    {
          input = (char) Serial.read();
          inputln += input;
    }
  }
}

void pinSet()
{
  if(inputln == "pinMode\n")
  {
  Serial.print("type number of pin\n");
  inputln = "";
  serialCom();
  integer = inputln.toInt();

  switch(integer)
  {
    case 22:
      Serial.print("select INPUT or OUTPUT\n");
      inputln = "";
      serialCom();
      if (inputln == "OUTPUT\n")
      {
        pinMode(dpin22, OUTPUT);
        Serial.print("pin 22 has been set to OUTPUT\n");
      }
      else if (inputln == "INPUT\n")
      {
        pinMode(dpin22, INPUT);
        Serial.print("pin 22 has been set to INPUT\n");
      }
      break;
    case 24:
      Serial.print("type INPUT or OUTPUT\n");
      inputln = "";
      serialCom();
      if (inputln == "OUTPUT\n")
      {
        pinMode(dpin24, OUTPUT);
        Serial.print("pin 24 has been set to OUTPUT\n");
      }
      else if (inputln == "INPUT\n")
      {
        pinMode(dpin24, INPUT);
        Serial.print("pin 24 has been set to INPUT\n");
      }
      break;
    case 26:
      Serial.print("type INPUT or OUTPUT\n");
      inputln = "";
      serialCom();
      if (inputln == "OUTPUT\n")
      {
        pinMode(dpin26, OUTPUT);
        Serial.print("pin 26 has been set to OUTPUT\n");
      }
      else if (inputln == "INPUT\n")
      {
        pinMode(dpin26, INPUT);
        Serial.print("pin 26 has been set to INPUT\n");
      }
      break;
    case 28:
      Serial.print("type INPUT or OUTPUT\n");
      inputln = "";
      serialCom();
      if (inputln == "OUTPUT\n")
      {
        pinMode(dpin28, OUTPUT);
      }
      else if (inputln == "INPUT\n")
      {
        pinMode(dpin28, INPUT);
      }
      break;
    }
  }
}

void pinVal22()
{
  if (inputln == "22 on\n")
  {
    digitalWrite(22, HIGH);
    Serial.print("pin 22 set to HIGH\n");
  }
  else if(inputln == "22 off\n")
  {
    digitalWrite(22, LOW);
    Serial.print("pin 22 set to LOW\n");
  }
}

void pinVal24()
{
  if (inputln == "24 on\n")
  {
    digitalWrite(24, HIGH);
    Serial.print("pin 24 set to HIGH\n");
  }
  else if(inputln == "24 off\n")
  {
    digitalWrite(24, LOW);
    Serial.print("pin 24 set to LOW\n");
  }
}

void pinVal26()
{
  if (inputln == "26 on\n")
  {
    digitalWrite(26, HIGH);
    Serial.print("pin 26 set to HIGH\n");
  }
  else if(inputln == "26 off\n")
  {
    digitalWrite(26, LOW);
    Serial.print("pin 26 set to LOW\n");
  }
}

void readSensor()
{
  int pin = 26;
  String state;
  if (inputln == "read sensor\n")
  {
    state = digitalRead(pin);
    Serial.print(state + "\n");
  }
}
