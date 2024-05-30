import cv2
import numpy as np

def nothing(x):
    pass

# Perulangan
while True:
    frame = cv2.imread('gambar.png')
    if frame is None:
        print("Image not found.")
        break

    # Konversi warna BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lower range warna merah
    lower_range = np.array([0, 100, 100])
    # Upper range warna merah
    upper_range = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Menampilkan gambar
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()