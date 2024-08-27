#made by following a tutorial and a shit ton of research since i'm a beginner lol
#made by Btn

import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

counter = 0

face_match = False
ref_mg = cv2.imread("your image")

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, ref_mg.copy())['verified']
        face_match = result
    except Exception as e:  # Catching all exceptions that might occur
        print(f"Error during face verification: {e}")
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 60 == 0:
            try:
                thread = threading.Thread(target=check_face, args=(frame.copy(),))
                thread.start()  # Start the thread
            except Exception as e:
                print(f"Threading error: {e}")
        counter += 1

        if face_match:
            cv2.putText(frame, "Passed!", (20, 650), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.putText(frame, "press k to break", (5, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 200, 200), 3)
        else:
            cv2.putText(frame, "No match!", (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.putText(frame, "press k to break", (5,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 200, 200), 3)
        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord('k'):
        break

cv2.destroyAllWindows()
cap.release()
