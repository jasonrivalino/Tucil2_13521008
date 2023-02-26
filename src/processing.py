import math
import time
import numpy as np
import inputting as input
from numpy import random

# Sorting untuk mengurutkan koordinat berdasarkan x membesar
def sortingX(listKoordinat):
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if listKoordinat[i][0] < listKoordinat[j][0]:
                listKoordinat[i], listKoordinat[j] = listKoordinat[j], listKoordinat[i]
    return listKoordinat

def sortingY(listKoordinat):
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if listKoordinat[i][1] < listKoordinat[j][1]:
                listKoordinat[i], listKoordinat[j] = listKoordinat[j], listKoordinat[i]
    return listKoordinat

hitungEuclidean = 0

# Melakukan proses brute force untuk mencari jarak terdekat (2D)
def bruteForce2D(listKoordinat):
    global hitungEuclidean
    jarak = []
    min = float("inf")
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                hitungEuclidean += 1
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))))
    for i in range (len(jarak)):
        if jarak[i] < min:
            min = jarak[i]
    return min

# Melakukan proses brute force untuk mencari jarak terdekat (3D)
def bruteForce3D(listKoordinat):
    global hitungEuclidean
    jarak = []
    min = float("inf")
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                hitungEuclidean += 1
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))+
                                       (pow((listKoordinat[j][2]-listKoordinat[i][2]),2))))
    for i in range (len(jarak)):
        if jarak[i] < min:
            min = jarak[i]
    return min

# Melakukan proses divide and conquer untuk mencari jarak terdekat (3D)
def divideAndConquer3D(listKoordinat, n, dimensi):
    n = len(listKoordinat)
    # Basis 1
    if n == 2:
        jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                          (pow((listKoordinat[1][1]-listKoordinat[0][1]),2))+
                          (pow((listKoordinat[1][2]-listKoordinat[0][2]),2)))
        return jarak
    # Basis 2
    elif n == 3:
        jarak1 = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                           (pow((listKoordinat[1][1]-listKoordinat[0][1]),2))+
                           (pow((listKoordinat[1][2]-listKoordinat[0][2]),2)))
        jarak2 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[0][0]),2))+
                           (pow((listKoordinat[2][1]-listKoordinat[0][1]),2))+
                           (pow((listKoordinat[2][2]-listKoordinat[0][2]),2)))
        jarak3 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[1][0]),2))+
                           (pow((listKoordinat[2][1]-listKoordinat[1][1]),2))+
                           (pow((listKoordinat[2][2]-listKoordinat[1][2]),2)))
        if jarak1 < jarak2 and jarak1 < jarak3:
            jarak = jarak1
        elif jarak2 < jarak1 and jarak2 < jarak3:
            jarak = jarak2
        else:
            jarak = jarak3
        return jarak
    else:
        # Membagi listKoordinat menjadi 2 bagian
        middle = n//2
        left_area = []
        right_area = []
        for i in range (middle):
            left_area.append(listKoordinat[i])
        for i in range (middle, n):
            right_area.append(listKoordinat[i])
        # print("Left: ", left_area)
        # print("Right: ", right_area)
        # Mencari jarak terdekat dari setiap bagian dengan rekursif
        jarak1 = divideAndConquer3D(left_area, n, dimensi)
        jarak2 = divideAndConquer3D(right_area, n, dimensi)
        # print("jarak1: ", jarak1)
        # print("jarak2: ", jarak2)
        if jarak1 < jarak2:
            jarak = jarak1
        else:
            jarak = jarak2
        # print("jarak: ", jarak)
        # Mencari jarak terdekat dari setiap titik yang berada di antara kedua bagian
        point_middle = listKoordinat[middle][0]
        strip = [p for p in listKoordinat if abs(p[0] - point_middle) < jarak]
        # print("strip: ", strip)
        strip_sorted = sortingY(strip)
        # print("strip_sorted: ", strip_sorted)
        for i in range (len(strip_sorted)):
            for j in range (i+1, len(strip_sorted)):
                if (strip_sorted[j][0] - strip_sorted[i][0]) >= jarak and (strip_sorted[j][1] - strip_sorted[i][1]) >= jarak:
                    break
                newJarak = math.sqrt((pow((strip_sorted[j][0]-strip_sorted[i][0]),2))+
                                     (pow((strip_sorted[j][1]-strip_sorted[i][1]),2))+
                                     (pow((strip_sorted[j][2]-strip_sorted[i][2]),2)))
                if newJarak < jarak:
                    jarak = newJarak
        # print("jarakbaru: ", jarak)
        return jarak