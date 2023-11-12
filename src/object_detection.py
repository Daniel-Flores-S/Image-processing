import cv2
import mediapipe as mp

def main():
    cap = cv2.VideoCapture(0)

    mp_holistic = mp.solutions.holistic
    holistic = mp_holistic.Holistic()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Converta a imagem para formato RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processar a imagem usando o modelo mediapipe para detecção holística
        results = holistic.process(rgb_frame)

        # Desenhar as detecções na imagem
        if results.right_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        if results.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow('Detecção Holística', frame)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
