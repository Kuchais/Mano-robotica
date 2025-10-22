import cv2
from cvzone.HandTrackingModule import HandDetector
from serial import Serial, SerialException
import time

#arduino = None
#try:
#    arduino = Serial("COM3", 9600, timeout=0.5)  # Ajusta el puerto COM según tu Arduino
#   time.sleep(2)  # Espera a que el puerto se estabilice
#except SerialException as e:
#    print(f"Error al abrir el puerto serial: {e}")
#    arduino = None

# Iniciar cámara
cap = cv2.VideoCapture(0)  # Cambia a 0 si tu cámara principal es otra
if not cap.isOpened():
    print('Error al abrir la cámara')
    exit()

# Detector de manos
detector = HandDetector(maxHands=1, detectionCon=0.8)

last_send_time = 0
send_interval = 0.2  # 200 ms entre envíos

try:
    while True:
        success, frame = cap.read()
        if not success:
            print("Error en la cámara, reintentando...")
            cap.release()
            time.sleep(1)
            cap = cv2.VideoCapture(1)
            continue
        
        manos, framePuntos = detector.findHands(frame)
        
        current_time = time.time()
        if manos and (current_time - last_send_time) > send_interval:
            mano = manos[0]
            dedos = detector.fingersUp(mano)
            datos = "".join(map(str, dedos)) + "\n"
            print (datos)
            
            #if arduino is not None:
             #   try:
              #      arduino.write(datos.encode())
               #     arduino.flush()
                #    last_send_time = current_time
               # except SerialException as e:
                #    print(f"Error serial: {e}")
                 #   arduino.close()
                  #  arduino = None

        cv2.imshow('Detección de manos', framePuntos)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    #if arduino is not None:
     #   arduino.close()
