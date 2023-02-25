import math
import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def inputTitik (n):
    n = int(input("Masukkan jumlah titik: "))
    return n

def inputKoordinatTigaDimensi(n):
    # dimensi = int(input("Masukkan dimensi: "))
    coordinates = []
    for i in range (n):
        x = random.randint(1,150)
        y = random.randint(1,150)
        z = random.randint(1,150)
        coordinates.append([x,y,z])
    return coordinates

# Sorting untuk mengurutkan koordinat berdasarkan x mengecil
def sorting(listKoordinat):
    listKoordinat.sort()
    return listKoordinat

def projectionBefore(listKoordinat):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Data untuk proyeksi 3D
    for i in range (len(listKoordinat)):
        np.linspace(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2])

        # Plotting titik-titik
        ax.scatter3D(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2], color='red')

    plt.show()

def bruteForce(listKoordinat):
    jarak = []
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+(pow((listKoordinat[j][1]-listKoordinat[i][1]),2))+(pow((listKoordinat[j][2]-listKoordinat[i][2]),2))))
    return jarak
    

# # Main program
# n = 0
# n = inputTitik(n)
# # print(n)
# listKoordinat = inputKoordinatTigaDimensi(n)
# # print("")
# # print("Titik-titik yang didapat adalah: ")
# # print(listKoordinat)
# # print("")
# # print("List koordinat setelah disorting: ")
# koordinatSorting = sorting(listKoordinat)
# # print(koordinatSorting)
# projectionBefore(koordinatSorting)
# print("")
# start_time = time.time()
# jarak = bruteForce(koordinatSorting)
# stop_time = time.time()
# print("Jarak terdekat antar titik dengan brute force:", min(jarak))