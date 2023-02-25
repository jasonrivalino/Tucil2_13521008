import inputting as input
import processing as process
import projection as project
import splash as splash
import time

# Opening Splash
splash.openingSplash()

# Insialisasi variabel
n = 0

# Input jumlah titik
n = input.inputTitik(n)

# Input dimensi
dimensi = input.inputDimension(n)

# Kondisi dimensi input
while (dimensi != 2 and dimensi != 3):
    dimensi = input.inputDimension(n)
if dimensi == 2:
    listKoordinat = input.inputKoordinatDuadimensi(n)
elif dimensi == 3:
    listKoordinat = input.inputKoordinatTigaDimensi(n)

# Melakukan proses sorting
koordinatSorting = process.sorting(listKoordinat)

# Proyeksi sebelum mencari jarak terdekat
if dimensi == 2:
    project.projectionBefore2D(koordinatSorting)
    print("")
    start_bf_time = time.time()
    jarak = process.bruteForce2D(koordinatSorting)
    stop_bf_time = time.time()
    # Menampilkan hasil dengan Algoritma Brute Force
    print("==============================================")
    print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
    print("Jarak terdekat antar titik:", min(jarak))
    print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
    print("==============================================")
elif dimensi == 3:
    project.projectionBefore3D(koordinatSorting)
    print("")
    start_bf_time = time.time()
    jarak = process.bruteForce3D(koordinatSorting)
    stop_bf_time = time.time()
    # Menampilkan hasil dengan Algoritma Brute Force
    print("==============================================")
    print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
    print("Jarak terdekat antar titik:", min(jarak))
    print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
    print("==============================================")