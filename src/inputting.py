import numpy as np
from numpy import random

# Melakukan input titik
def inputTitik (n):
    n = int(input("Masukkan jumlah titik (1-1000): "))
    while (n < 2 or n > 1000):
        n = int(input("Masukkan jumlah titik (1-1000): "))
    return n

# Melakukan input dimensi
def inputDimension (n):
    print("Opsi Pilihan:")
    print("A) Mencari titik pada 2 dimensi")
    print("B) Mencari titik pada 3 dimensi")
    n = input("Masukkan pilihan: ")
    while (n != "A" and n != "a" and n != "B" and n != "b"):
        n = input("Masukkan pilihan (A/B): ")
    return n

# Melakukan input koordinat dengan pembangkit bilangan acak (2D)
def inputKoordinatDuaDimensi(n):
    coordinates = []
    for i in range (n):
        x = random.randint(1,200)
        y = random.randint(1,200)
        coordinates.append([x,y])
    return coordinates

# Melakukan input koordinat dengan pembangkit bilangan acak (3D)
def inputKoordinatTigaDimensi(n):
    coordinates = []
    for i in range (n):
        x = random.randint(1,200)
        y = random.randint(1,200)
        z = random.randint(1,200)
        coordinates.append([x,y,z])
    # print(coordinates)
    return coordinates