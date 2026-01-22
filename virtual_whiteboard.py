import cv2
import mediapipe as mp
import os

dispositivoCaptura = cv2.VideoCapture(0)

dispositivoCaptura.set(3, 1280)
dispositivoCaptura.set(4, 740)
mpManos = mp.solutions.hands

manos = mpManos.Hands(static_image_mode=False,
                    max_num_hands=1, 
                    min_detection_confidence=0.9, 
                    min_tracking_confidence=0.8)

mpDibujar = mp.solutions.drawing_utils  

puntos_dibujo = []

while True:
    success, img = dispositivoCaptura.read()
    
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    resultado = manos.process(imgRGB)

    rojo = cv2.circle(img, (1200, 70), 25, (0, 0, 255), cv2.FILLED)

    if resultado.multi_hand_landmarks:
        for h, handLms in enumerate(resultado.multi_hand_landmarks):
            mpDibujar.draw_landmarks(img, handLms, mpManos.HAND_CONNECTIONS)

            punta_indice = handLms.landmark[8] 
            nudillo_indice = handLms.landmark[6]

            punta_medio = handLms.landmark[12]
            nudillo_medio = handLms.landmark[10]

            punta_anular = handLms.landmark[16]
            nudillo_anular = handLms.landmark[14]

            xi = int(punta_indice.x * 1280)
            yi = int(punta_indice.y * 740)

            xm = int(punta_medio.x * 1280)
            ym = int(punta_medio.y * 740)

            pincel = cv2.circle(img, (xi, yi), 15, (0, 255, 0), cv2.FILLED)

            indice_arriba = punta_indice.y < nudillo_indice.y
            
            medio_arriba = punta_medio.y < nudillo_medio.y
            medio_abajo = punta_medio.y > nudillo_medio.y

            anular_arriba = punta_anular.y < nudillo_anular.y
           
            if anular_arriba and medio_arriba and indice_arriba:
                print("Borrando")
                puntos_dibujo = []
            elif medio_arriba and indice_arriba:
                print("No dibujando")
                cv2.circle(img, (xi, yi), 15, (0, 0, 255), cv2.FILLED)
            elif indice_arriba and medio_abajo:
                pincel
                print("Dibujando")
                puntos_dibujo.append((xi, yi))
            
            for punto in puntos_dibujo:
                cv2.circle(img, punto, 10, (255, 0, 255), cv2.FILLED)


            
                
    cv2.imshow("Pizarra virtual", img)
    cv2.waitKey(1)
