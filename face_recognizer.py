import cv2
import face_recognition
import os

stored_faces = []
faces_names = []


def recognize_face(encoding_img):  # If the face in system, it gives name
    match = face_recognition.compare_faces(stored_faces, encoding_img)
    try:
        return faces_names[match.index(True)]
    except ValueError:
        return None


def add_face(): # Add face to the system by using cam
    camera = cv2.VideoCapture(0)
    i = 0
    while i < 10:
        ret, frame = camera.read()
        face_locations = face_recognition.face_locations(frame)
        i = i + 1  # In the first frame camera sometimes doesn't detect someone
        if i == 10 and len(face_locations) > 1:
            print("Too much faces")
        elif i == 10 and len(face_locations) < 1:
            print("There are no faces")
        elif len(face_locations) == 1:
            face = face_locations[0]
            cv2.rectangle(frame, (face[3], face[0]), (face[1], face[2]), (255, 0, 0), 2)
            cv2.imshow("Result", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            name = input("Please enter the name: ")
            newimg = frame[face[0]:face[2], face[3]: face[1]]
            cv2.imwrite("known_faces/"+str(name)+".jpg", newimg)
            cv2.destroyAllWindows()
            camera.release()
            break


def complete_faces(): # Get all faces from filesystem and be ready to recognize faces
    images = os.listdir("known_faces")
    names = [x[:x.index(".")] for x in images]
    for image, name in zip(images, names):
        read_img = cv2.imread("known_faces/"+image)
        new_face = face_recognition.face_encodings(read_img)[0]
        stored_faces.append(new_face)
        faces_names.append(name)


if __name__ == "face_recognizer":
    complete_faces()
elif __name__ == "__main__":
    add_face()
