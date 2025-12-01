import cv2

def extract_frames(video_path, frame_rate=5):
    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % frame_rate == 0:
            frames.append(frame)
        frame_id += 1
    cap.release()
    return frames
