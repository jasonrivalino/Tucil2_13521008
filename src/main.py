import inputting as inp
import processing as process
import projection as project
import splash as splash
import time

# Opening Splash
splash.openingSplash()

keluarProgram = False
process.hitungEuclideanBF = 0
process.hitungEuclideanDC = 0

while (keluarProgram == False):
    # Insialisasi variabel
    n = 0

    # Input jumlah titik
    n = inp.inputTitik(n)

    # Input dimensi
    print("")
    dimensi = inp.inputDimension(n)

    # Kondisi dimensi input
    if dimensi == "A" or dimensi == "a":
        listKoordinat = inp.inputKoordinatDuaDimensi(n)
    elif dimensi == "B" or dimensi == "b":
        listKoordinat = inp.inputKoordinatTigaDimensi(n)

    # Melakukan proses sorting
    koordinatSorting = process.sortingX(listKoordinat)

    # process.divideAndConquer3D(koordinatSorting, len(koordinatSorting))

    # Proyeksi sebelum mencari jarak terdekat
    if dimensi == "A" or dimensi == "a":
        project.projectionBefore2D(koordinatSorting)
        print("")
        start_bf_time = time.time()
        jarak = process.bruteForce2D(koordinatSorting)
        stop_bf_time = time.time()
        # Menampilkan hasil dengan Algoritma Brute Force
        print("==============================================")
        print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
        print("----------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanBF)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("==============================================")
        print("")
        print("==============================================")
        start_bf_time = time.time()
        jarak = process.divideAndConquer2D(koordinatSorting, len(koordinatSorting), 3)
        stop_bf_time = time.time()
        print("MENCARI DENGAN ALGORITMA DIVIDE AND CONQUER")
        print("----------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanDC)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("==============================================")
        

    elif dimensi == "B" or dimensi == "b":
        project.projectionBefore3D(koordinatSorting)
        print("")
        start_bf_time = time.time()
        jarak = process.bruteForce3D(koordinatSorting)
        stop_bf_time = time.time()
        # Menampilkan hasil dengan Algoritma Brute Force
        print("==============================================")
        print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanBF)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("==============================================")
        start_bf_time = time.time()
        jarak = process.divideAndConquer3D(koordinatSorting, len(koordinatSorting), 3)
        stop_bf_time = time.time()
        print("MENCARI DENGAN ALGORITMA DIVIDE AND CONQUER")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanDC)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("==============================================")

    print("")
    question = input("Apakah anda ingin mencari titik terdekat lagi? (Y/N): ")
    if question == "Y" or question == "y":
        keluarProgram = False
    elif question == "N" or question == "n":
        keluarProgram = True

# Closing Splash
splash.closingSplash()