import cv2
import time

# Carregar o classificador pré-treinado para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a webcam
cap = cv2.VideoCapture(0)  # Tente ajustar o índice se necessário (por exemplo, 1)

# Adicione um pequeno atraso para lidar com possíveis problemas de inicialização
time.sleep(1)

while True:
    # Capturar o frame da webcam
    ret, frame = cap.read()

    # Verificar se o frame foi capturado corretamente
    if not ret:
        print("Erro ao capturar o frame.")
        break

    # Converter para escala de cinza para a detecção de rostos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exibir o frame resultante
    cv2.imshow('Detecção de Rostos', frame)

    # Encerrar o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
