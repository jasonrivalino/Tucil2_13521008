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

    print("Menampilkan Proyeksi Titik Koordinat...")
    plt.show()