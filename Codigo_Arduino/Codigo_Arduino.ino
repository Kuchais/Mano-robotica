#include <Servo.h>

Servo servoThumb;   // Pulgar
Servo servoIndex;   // Índice
Servo servoMiddle;  // Medio
Servo servoRing;    // Anular
Servo servoPinky;   // Meñique

int valsRec[5] = {0, 0, 0, 0, 0}; 
String receivedString = "";       
bool newData = false;             

void setup() {
  Serial.begin(9600);

  servoThumb.attach(6);   
  servoIndex.attach(9);   
  servoMiddle.attach(11); 
  servoRing.attach(8);    
  servoPinky.attach(10);  

  // Posición inicial
  servoThumb.write(180);
  servoIndex.write(180);
  servoMiddle.write(180);
  servoRing.write(60);
  servoPinky.write(180);
}

void receiveData() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      newData = true;
      break;
    } else {
      receivedString += c; 
    }
  }
}

void processData() {
  if (newData) {
    if (receivedString.length() == 5) {
      for (int i = 0; i < 5; i++) {
        valsRec[i] = receivedString[i] - '0'; 
      }

      // Mover servos según los valores recibidos
      servoThumb.write(valsRec[0] == 1 ? 180 : 120);
      servoIndex.write(valsRec[1] == 1 ? 180 : 0);
      servoMiddle.write(valsRec[2] == 1 ? 180 : 0);
      servoRing.write(valsRec[3] == 1 ? 60 : 180);
      servoPinky.write(valsRec[4] == 1 ? 180 : 0);
    }

    receivedString = "";
    newData = false;
  }
}

void loop() {
  receiveData(); 
  processData(); 
  delay(10); // Pequeño delay para estabilidad
}
