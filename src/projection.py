import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def projectionBefore2D(listKoordinat):
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')
    print("Menampilkan Proyeksi Titik Koordinat...")
    plt.show()

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

def projectionAfter2D(listKoordinat, listKoordinatTerdekat):
    for i in range (len(listKoordinat)):
        plt.scatter(listKoordinat[i][0], listKoordinat[i][1], color='red')

    for i in range (len(listKoordinatTerdekat)):
        plt.scatter(listKoordinatTerdekat[i][0], listKoordinatTerdekat[i][1], color='blue')

    print("")
    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    plt.show()

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

    print("")
    print("Menampilkan Proyeksi Titik Koordinat Terdekat...")
    plt.show()