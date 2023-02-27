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

hitungEuclideanBF = 0

# Melakukan proses brute force untuk mencari jarak terdekat (2D)
def bruteForce2D(listKoordinat):
    global hitungEuclideanBF
    jarak = []
    min = float("inf")
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))))
                hitungEuclideanBF += 1
    for i in range (len(jarak)):
        if jarak[i] < min:
            min = jarak[i]
    return min

# Melakukan proses brute force untuk mencari jarak terdekat (3D)
def bruteForce3D(listKoordinat):
    global hitungEuclideanBF
    jarak = []
    min = float("inf")
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                       (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))+
                                       (pow((listKoordinat[j][2]-listKoordinat[i][2]),2))))
                hitungEuclideanBF += 1
    for i in range (len(jarak)):
        if jarak[i] < min:
            min = jarak[i]
    return min

hitungEuclideanDC = 0

# Melakukan proses divide and conquer untuk mencari jarak terdekat (2D)
def divideAndConquer2D(listKoordinat, n, dimensi):
    global hitungEuclideanDC
    n = len(listKoordinat)
    # Basis 1
    if n == 2:
        jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                          (pow((listKoordinat[1][1]-listKoordinat[0][1]),2)))
        hitungEuclideanDC += 1
        tempNearest = [listKoordinat[0], listKoordinat[1]]
        return jarak, tempNearest
    # Basis 2
    elif n == 3:
        jarak1 = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                           (pow((listKoordinat[1][1]-listKoordinat[0][1]),2)))
        jarak2 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[0][0]),2))+
                           (pow((listKoordinat[2][1]-listKoordinat[0][1]),2)))
        jarak3 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[1][0]),2))+
                           (pow((listKoordinat[2][1]-listKoordinat[1][1]),2)))
        if jarak1 < jarak2 and jarak1 < jarak3:
            hitungEuclideanDC += 1
            jarak = jarak1
            tempNearest = [listKoordinat[0], listKoordinat[1]]
        elif jarak2 < jarak1 and jarak2 < jarak3:
            hitungEuclideanDC += 1
            jarak = jarak2
            tempNearest = [listKoordinat[0], listKoordinat[2]]
        else:
            hitungEuclideanDC += 1
            jarak = jarak3
            tempNearest = [listKoordinat[1], listKoordinat[2]]
        return jarak, tempNearest
    else:
        # Membagi data menjadi 2 bagian
        middle = n//2
        left_area = []
        right_area = []
        for i in range (middle):
            left_area.append(listKoordinat[i])
        for i in range (middle, n):
            right_area.append(listKoordinat[i])
        # Mencari jarak terdekat di kiri dan kanan
        jarak1, koordinat1 = divideAndConquer2D(left_area,middle, dimensi)
        hitungEuclideanDC += 1
        jarak2, koordinat2 = divideAndConquer2D(right_area,middle, dimensi)
        hitungEuclideanDC += 1
        # Mencari jarak terdekat di antara kiri dan kanan
        jarak = min(jarak1, jarak2)
        if jarak == jarak1:
            tempNearest = koordinat1
        elif jarak == jarak2:
            tempNearest = koordinat2
        # Mencari jarak terdekat di antara kiri dan kanan berdasarkan x tengah
        strip = []
        for i in range (n):
            if listKoordinat[i][0] >= (listKoordinat[middle][0]-jarak) and listKoordinat[i][0] <= (listKoordinat[middle][0]+jarak):
                strip.append(listKoordinat[i])
        # Mencari jarak terdekat di antara kiri dan kanan berdasarkan y tengah
        strip_sorted = sortingY(strip)
        for i in range (len(strip_sorted)):
            for j in range (i+1, len(strip_sorted)):
                if (strip_sorted[j][0] - strip_sorted[i][0]) >= jarak and (strip_sorted[j][1] - strip_sorted[i][1]) >= jarak:
                    break
                newJarak = math.sqrt((pow((strip_sorted[j][0]-strip_sorted[i][0]),2))+
                                     (pow((strip_sorted[j][1]-strip_sorted[i][1]),2)))
                if newJarak < jarak:
                    jarak = newJarak
                    tempNearest = [strip_sorted[i], strip_sorted[j]]
                    hitungEuclideanDC += 1
        return jarak, tempNearest


# Melakukan proses divide and conquer untuk mencari jarak terdekat (3D)
def divideAndConquer3D(listKoordinat, n, dimensi):
    global hitungEuclideanDC
    n = len(listKoordinat)
    # Basis 1
    if n == 2:
        jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                          (pow((listKoordinat[1][1]-listKoordinat[0][1]),2))+
                          (pow((listKoordinat[1][2]-listKoordinat[0][2]),2)))
        hitungEuclideanDC += 1
        tempNearest = [listKoordinat[0], listKoordinat[1]]
        # print(tempNearest)
        return jarak, tempNearest
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
            tempNearest = [listKoordinat[0], listKoordinat[1]]
            # print(tempNearest)
            hitungEuclideanDC += 1
        elif jarak2 < jarak1 and jarak2 < jarak3:
            jarak = jarak2
            tempNearest = [listKoordinat[0], listKoordinat[2]]
            # print(tempNearest)
            hitungEuclideanDC += 1
        else:
            jarak = jarak3
            tempNearest = [listKoordinat[1], listKoordinat[2]]
            # print(tempNearest)
            hitungEuclideanDC += 1
        return jarak, tempNearest
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
        jarak1, koordinat1 = divideAndConquer3D(left_area, n, dimensi)
        hitungEuclideanDC += 1
        jarak2, koordinat2 = divideAndConquer3D(right_area, n, dimensi)
        hitungEuclideanDC += 1
        # print("jarak1: ", jarak1)
        # print("jarak2: ", jarak2)
        if jarak1 < jarak2:
            jarak = jarak1
            tempNearest = koordinat1

        else:
            jarak = jarak2
            tempNearest = koordinat2
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
                    tempNearest = [strip_sorted[i], strip_sorted[j]]
                    hitungEuclideanDC += 1
        # print("jarakbaru: ", jarak)
        return jarak, tempNearest