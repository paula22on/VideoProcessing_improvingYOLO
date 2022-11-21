# This file contaibns code to invert the colors of an image

import cv2
import numpy as np
import sys

def inverte(imagem, name):
    imagem = abs(255 - imagem)
    cv2.imwrite(name, imagem)


def inverte2(imagem, name):
    for x in np.nditer(imagem, op_flags=['readwrite']):
        x = abs(x - 255)
    cv2.imwrite(name, imagem)

image = cv2.imread('images/Riyadh_people.png')
gs_imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverte(gs_imagem, "images/Riyadh_people_inverted1.png")
inverte2(gs_imagem, "images/Riyadh_people_inverted2.png")