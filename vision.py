# Bilderkennung
# Start 13.5.22 mit https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

import cv2 as cv
import numpy as np
import sys


def show(img, duration):
    cv.namedWindow("Kartenset", cv.WINDOW_NORMAL)  # Create window with freedom of dimensions
    cv.moveWindow("Kartenset", 80, 20)
    cv.imshow("Kartenset", img)
    cv.resizeWindow("Kartenset", 600, 800)
    cv.waitKey(int(duration * 1000))  # Bild bleibt x ms oder bis Taste gedrückt wird


def analyse(img):

    # Öffnen
    img_orig = cv.imread(img_path)
    if img_orig is None:
        sys.exit("Could not read the image.")
    # show(img_orig, 1)

    # Graustufen
    img_gray = cv.imread(img, cv.IMREAD_GRAYSCALE)
    # show(img_gray, 1)

    # Binarisieren
    # ret, img_bin = cv.threshold(img_gray, 170, 255, cv.THRESH_BINARY)
    # img_bin = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21,15)  # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

    # Otsu's thresholding after Gaussian filtering
    img_gray = cv.GaussianBlur(img_gray, (5, 5), 0)
    ret, img_bin = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    show(img_bin, 1)

    # Konturen erkennen
    contours, hierarchy = cv.findContours(img_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img_orig, contours, -1, (255, 0, 255), 3)

    return img_orig


img_path = "Photos/Set-2_dunkel-lose-gerade.jpg"
img = analyse(img_path)
show(img, 9)
