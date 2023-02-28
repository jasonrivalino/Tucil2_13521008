import numpy as np
from numpy import random

# Melakukan input jumlah titik yang ingin dihitung
def inputTitik (n):
    n = int(input("Masukkan jumlah titik (2-1000): "))
    while (n < 2 or n > 1000):
        n = int(input("Masukkan jumlah titik (2-1000): "))
    return n

# Melakukan input dimensi
def inputDimension (n):
    print("Opsi Pilihan:")
    print("1) Mencari titik pada 1 dimensi")
    print("2) Mencari titik pada 2 dimensi")
    print("3) Mencari titik pada 3 dimensi")
    n = int(input("Masukkan pilihan dimensi: "))
    while (n != 1 and n != 2 and n != 3):
        n = int(input("Masukkan pilihan dimensi: "))
    return n

# Melakukan input koordinat dengan pembangkit bilangan acak
def inputKoordinat(n,dimensi):
    coordinates = []
    for i in range (n):
        if (dimensi == 1):
            x = random.randint(1,1000)
            coordinates.append([x])
        elif (dimensi == 2):
            x = random.randint(1,250)
            y = random.randint(1,250)
            coordinates.append([x,y])
        elif (dimensi == 3):
            x = random.randint(1,250)
            y = random.randint(1,250)
            z = random.randint(1,250)
            coordinates.append([x,y,z])
    return coordinates