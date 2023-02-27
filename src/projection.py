import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Fungsi proyeksi awal 1D
def projectionBefore1D(listKoordinat):
    # Data untuk proyeksi 1D
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], 0, color='red')
    print("Menampilkan Proyeksi Titik Koordinat...")
    plt.show()    

# Fungsi proyeksi awal 2D
def projectionBefore2D(listKoordinat):
    # Data untuk proyeksi 2D
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')
    print("Menampilkan Proyeksi Titik Koordinat...")
    plt.show()

# Fungsi proyeksi awal 3D
def projectionBefore3D(listKoordinat):
    fig = plt.figure()
    axes = plt.axes(projection='3d')

    # Data untuk proyeksi 3D
    for i in range (len(listKoordinat)):
        np.linspace(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2])

        # Plotting titik-titik
        axes.scatter3D(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2], color='red')

    print("Menampilkan Proyeksi Titik Koordinat Awal...")
    plt.show()

# Fungsi proyeksi jarak titik terdekat 1D
def projectionAfter1D(listKoordinat, listKoordinatTerdekat):
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], 0, color='red')
    
    for i in range (len(listKoordinatTerdekat)):
        plt.scatter(listKoordinatTerdekat[i][0], 0, color='blue')
        
    print("Menampilkan Proyeksi Titik Koordinat...")
    plt.show()  

# Fungsi proyeksi jarak titik terdekat 2D
def projectionAfter2D(listKoordinat, listKoordinatTerdekat):
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')

    for i in range (len(listKoordinatTerdekat)):
        plt.scatter(listKoordinatTerdekat[i][0], listKoordinatTerdekat[i][1], color='blue')

    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    plt.show()

# Fungsi proyeksi jarak titik terdekat 3D
def projectionAfter3D(listKoordinat, listKoordinatTerdekat):
    fig = plt.figure()
    axes = plt.axes(projection='3d')

    # Data untuk proyeksi 3D
    for i in range (len(listKoordinat)):
        np.linspace(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2])

        # Plotting titik-titik
        axes.scatter3D(listKoordinat[i][0], listKoordinat[i][1], listKoordinat[i][2], color='red')

    # Plotting garis antara titik terdekat
    for i in range (len(listKoordinatTerdekat)):
        axes.scatter3D(listKoordinatTerdekat[i][0], listKoordinatTerdekat[i][1], listKoordinatTerdekat[i][2], color='blue')

    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    plt.show()