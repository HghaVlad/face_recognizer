import cv2
import face_recognition
from face_recognizer import recognize_face


camera = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_DUPLEX
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 128, 0), (128, 128, 128), (255, 128, 0), (0, 255, 255)]

while True:
    ret, frame = camera.read()
    face_locations = face_recognition.face_locations(frame)  # Get all faces locations
    face_encodigns = face_recognition.face_encodings(frame)  # Recongize all faces
    i = 0
    for face, encoded_face in zip(face_locations, face_encodigns):
        name = recognize_face(encoded_face)
        cv2.rectangle(frame, (face[3], face[0]), (face[1], face[2]), colors[i], 2)
        cv2.rectangle(frame, (face[3], face[2] - 25), (face[1], face[2]), colors[i], cv2.FILLED)
        if name is not None:
            cv2.putText(frame, name, (face[3] + 6, face[2] - 6), font, 0.5, (255, 255, 255), 1)
        else:
            cv2.putText(frame, "Unknown", (face[3] + 6, face[2] - 6), font, 0.5, (255, 255, 255), 1)
        i += 1

    cv2.imshow("Result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()