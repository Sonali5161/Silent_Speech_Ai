import mediapipe as mp
import cv2

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # Access the landmarks for the mouth region (e.g., points 61-78 for the mouth)
            mouth_points = [landmarks.landmark[i] for i in range(61, 81)]
            # Extract mouth region (you can crop or highlight it)
            # This can be extended to crop or analyze specific lip shapes

    cv2.imshow("Live Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
