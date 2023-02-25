import math
import time
import numpy as np
from numpy import random

# Sorting untuk mengurutkan koordinat berdasarkan x mengecil
def sorting(listKoordinat):
    listKoordinat.sort()
    return listKoordinat

# Melakukan proses brute force untuk mencari jarak terdekat (2D)
def bruteForce2D(listKoordinat):
    jarak = []
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))))
    return jarak

# Melakukan proses brute force untuk mencari jarak terdekat (3D)
def bruteForce3D(listKoordinat):
    jarak = []
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))+
                                       (pow((listKoordinat[j][2]-listKoordinat[i][2]),2))))
    return jarak