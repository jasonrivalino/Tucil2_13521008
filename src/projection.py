import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Fungsi untuk menampilkan proyeksi awal
def projectionBefore(listKoordinat, dimensi):
    if dimensi == 1:
        projectionBefore1D(listKoordinat)
    elif dimensi == 2:
        projectionBefore2D(listKoordinat)
    elif dimensi == 3:
        projectionBefore3D(listKoordinat)
    
# Fungsi untuk menampilkan proyeksi jarak titik terdekat
def projectionAfter(listKoordinat, listKoordinatTerdekat, dimensi):
    if dimensi == 1:
        projectionAfter1D(listKoordinat, listKoordinatTerdekat)
    elif dimensi == 2:
        projectionAfter2D(listKoordinat, listKoordinatTerdekat)
    elif dimensi == 3:
        projectionAfter3D(listKoordinat, listKoordinatTerdekat)

# Fungsi proyeksi awal 1D
def projectionBefore1D(listKoordinat):
    # Data untuk proyeksi 1D
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], 0, color='red')
    print("Menampilkan Proyeksi Titik Koordinat Awal...")
    plt.show()    

# Fungsi proyeksi awal 2D
def projectionBefore2D(listKoordinat):
    # Data untuk proyeksi 2D
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')
    print("Menampilkan Proyeksi Titik Koordinat Awal...")
    plt.show()

# Fungsi proyeksi awal 3D
def projectionBefore3D(listKoordinat):
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
        
    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    print("==============================================================")
    plt.show()  

# Fungsi proyeksi jarak titik terdekat 2D
def projectionAfter2D(listKoordinat, listKoordinatTerdekat):
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')

    for i in range (len(listKoordinatTerdekat)):
        plt.scatter(listKoordinatTerdekat[i][0], listKoordinatTerdekat[i][1], color='blue')

    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    print("==============================================================")
    plt.show()

# Fungsi proyeksi jarak titik terdekat 3D
def projectionAfter3D(listKoordinat, listKoordinatTerdekat):
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
    print("==============================================================")
    plt.show()