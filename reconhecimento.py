import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key

# Inicializa a webcam e o detector de mãos
webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=1)
keyboard = Controller()

#Detectando as mãos na imagem e retorna sua coordenada
while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    #Verificando se há pelo menos 21 pontos de referência para uma mão completa
    if coordenadas:
        for mao in coordenadas:
            landmarks = mao['lmList']
            if len(landmarks) >= 21:
                thumb_tip_y = landmarks[4][1]
                index_tip_y = landmarks[8][1]
                

                # Detecção de gesto: mover a mão para cima e para baixo
                if index_tip_y < thumb_tip_y:

                    # Polegar para baixo, diminui o volume
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                
                elif index_tip_y > thumb_tip_y:
                    # Polegar para cima, aumenta o volume
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)

    cv2.imshow("Controle de Volume", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()
