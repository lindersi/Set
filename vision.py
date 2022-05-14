# Bilderkennung
# Start 13.5.22 mit https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

import cv2 as cv
import sys


def show(img):
    cv.namedWindow("Kartenset", cv.WINDOW_NORMAL)  # Create window with freedom of dimensions
    cv.moveWindow("Kartenset", 80, 20)
    cv.imshow("Kartenset", img)
    cv.resizeWindow("Kartenset", 600, 800)
    cv.waitKey(3000)  # Bild bleibt x ms oder bis Taste gedrückt wird


# Bild öffnen und in definiertem Fenster anzeigen
img = cv.imread("Photos/Set-2_dunkel-lose-gerade.jpg")

if img is None:
    sys.exit("Could not read the image.")

# show(img)


# Karten-Konturen suchen
# Zuerst binarisieren... - allerdings gibt das Fehlermeldungen...

# img = cv.threshold(img, 170, 255, cv.THRESH_BINARY)
# img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)  # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

# ...dann Sobel oder Laplace (funktioniert, aber bringt ohne Binarisierung nicht viel)
# img = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=15)

# ...oder Canny Edge detection (funktioniert, aber nützt mir wahrscheinlich nichts)
img = cv.Canny(img, 100, 200)

show(img)
