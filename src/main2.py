import math
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Inisiasi variabel
print("Memasukkan titik koordinat pertama")
x1 = int(input("Masukkan nilai x1: "))
y1 = int(input("Masukkan nilai y1: "))
z1 = int(input("Masukkan nilai z1: "))
print("")
print("Memasukkan titik koordinat kedua")
x2 = int(input("Masukkan nilai x2: "))
y2 = int(input("Masukkan nilai y2: "))
z2 = int(input("Masukkan nilai z2: "))
print("")
print("Memasukkan titik koordinat ketiga")
x3 = int(input("Masukkan nilai x3: "))
y3 = int(input("Masukkan nilai y3: "))
z3 = int(input("Masukkan nilai z3: "))

# Menghitung jarak terdekat
jarak1 = math.sqrt((pow((x2-x1),2))+(pow((y2-y1),2))+(pow((z2-z1),2)))
jarak2 = math.sqrt((pow((x3-x1),2))+(pow((y3-y1),2))+(pow((z3-z1),2)))
jarak3 = math.sqrt((pow((x3-x2),2))+(pow((y3-y2),2))+(pow((z3-z2),2)))

print("")

# Memproyeksikan titik-titik ke bidang 3D
fig = plt.figure()
ax = plt.axes(projection='3d')

# Data untuk proyeksi 3D
x = np.linspace(x1, y1, z1)
y = np.linspace(x2, y2, z2)
z = np.linspace(x3, y3, z3)

# Plotting titik-titik
ax.scatter3D(x1, y1, z1, color='red')
ax.scatter3D(x2, y2, z2, color='blue')
ax.scatter3D(x3, y3, z3, color='green')

plt.show()

# Memulai waktu perhitungan
start_time = time.time()

# Menentukan jarak terdekat
if jarak1 < jarak2 and jarak1 < jarak3:
    print("Titik terdekat adalah titik 1 dan titik 2")
    print("Jarak kedua titiknya adalah", jarak1)
    stop_time = time.time()
    total_time = stop_time - start_time
    print("Waktu menjalankan program: %.7s detik" % (stop_time - start_time))

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x = np.linspace(x1, y1, z1)
    y = np.linspace(x2, y2, z2)
    z = np.linspace(x3, y3, z3)

    ax.scatter3D(x1, y1, z1, color='black')
    ax.scatter3D(x2, y2, z2, color='black')
    ax.scatter3D(x3, y3, z3, color='grey')

    plt.show()

elif jarak2 < jarak1 and jarak2 < jarak3:
    print("Titik terdekat adalah titik 1 dan titik 3")
    print("Jarak kedua titiknya adalah", jarak2)
    stop_time = time.time()
    total_time = stop_time - start_time
    print("Waktu menjalankan program: %.7s detik" % (stop_time - start_time))

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x = np.linspace(x1, y1, z1)
    y = np.linspace(x2, y2, z2)
    z = np.linspace(x3, y3, z3)

    ax.scatter3D(x1, y1, z1, color='black')
    ax.scatter3D(x2, y2, z2, color='grey')
    ax.scatter3D(x3, y3, z3, color='black')

    plt.show()
    
else:
    print("Titik terdekat adalah titik 2 dan titik 3")
    print("Jarak kedua titiknya adalah", jarak3)
    stop_time = time.time()
    total_time = stop_time - start_time
    print("Waktu menjalankan program: %.7s detik" % (stop_time - start_time))

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x = np.linspace(x1, y1, z1)
    y = np.linspace(x2, y2, z2)
    z = np.linspace(x3, y3, z3)

    ax.scatter3D(x1, y1, z1, color='black')
    ax.scatter3D(x2, y2, z2, color='black')
    ax.scatter3D(x3, y3, z3, color='grey')

    plt.show()