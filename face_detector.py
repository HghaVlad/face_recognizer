import cv2
import face_recognition

img = cv2.imread("example_img.jpg")
rgb_frame = img[:, :, ::-1]

face_locations = face_recognition.face_locations(rgb_frame)
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 128, 0), (128, 128, 128), (255, 128, 0), (0, 255, 255)]

i = 0 # Maximum amount of faces is 9(size of colors)
for top, right, bottom, left in face_locations:
    cv2.rectangle(img, (left, top), (right, bottom), colors[i], 2)
    i+=1

cv2.imwrite("newimage.jpg", img)

# Detect all faces in the image
