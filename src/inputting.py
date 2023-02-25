import numpy as np
from numpy import random

# Melakukan input titik
def inputTitik (n):
    n = int(input("Masukkan jumlah titik: "))
    return n

# Melakukan input dimensi
def inputDimension (n):
    n = int(input("Masukkan dimensi: "))
    return n

# Melakukan input koordinat dengan pembangkit bilangan acak (2D)
def inputKoordinatDuadimensi(n):
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
    return coordinates