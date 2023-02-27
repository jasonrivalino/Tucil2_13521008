import inputting as inp
import processing as process
import projection as project
import splash as splash
import time

# Opening Splash
splash.openingSplash()

# Inisialisasi variabel
keluarProgram = False
process.hitungEuclideanBF = 0
process.hitungEuclideanDC = 0
n = 0

while (keluarProgram == False):
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

    # Kondisi dimensi input
    if dimensi == "A" or dimensi == "a":
        # Proyeksi sebelum mencari jarak terdekat
        project.projectionBefore2D(koordinatSorting)

        print("")

        # Melakukan proses brute force
        start_bf_time = time.time()
        jarak = process.bruteForce2D(koordinatSorting)
        stop_bf_time = time.time()
        
        # Menampilkan hasil dengan Algoritma Brute Force
        print("=============================================================")
        print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
        print("-------------------------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanBF)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("=============================================================")

        print("")

        # Melakukan proses divide and conquer
        start_bf_time = time.time()
        jarak, koordinat = process.divideAndConquer2D(koordinatSorting, len(koordinatSorting), 3)
        stop_bf_time = time.time()

        # Menampilkan hasil dengan Algoritma Divide and Conquer
        print("=============================================================")
        print("MENCARI DENGAN ALGORITMA DIVIDE AND CONQUER")
        print("-------------------------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanDC)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("=============================================================")

        print("")

        # Menampilkan koordinat titik terdekat dan proyeksinya
        print("=============================================================")
        print("Koordinat titik terdekat: ", koordinat)
        project.projectionAfter2D(koordinatSorting, koordinat)
        print("=============================================================")
        

    elif dimensi == "B" or dimensi == "b":
        # Proyeksi sebelum mencari jarak terdekat
        project.projectionBefore3D(koordinatSorting)

        print("")

        # Melakukan proses brute force
        start_bf_time = time.time()
        jarak = process.bruteForce3D(koordinatSorting)
        stop_bf_time = time.time()

        # Menampilkan hasil dengan Algoritma Brute Force
        print("=============================================================")
        print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
        print("-------------------------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanBF)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("=============================================================")

        print("")
        
        # Melakukan proses divide and conquer
        start_bf_time = time.time()
        jarak, koordinat = process.divideAndConquer3D(koordinatSorting, len(koordinatSorting), 3)
        stop_bf_time = time.time()

        # Menampilkan hasil dengan Algoritma Divide and Conquer
        print("=============================================================")
        print("MENCARI DENGAN ALGORITMA DIVIDE AND CONQUER")
        print("-------------------------------------------------------------")
        print("Jarak terdekat antar titik:", jarak)
        print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanDC)
        print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
        print("=============================================================")

        print("")
        
        # Menampilkan koordinat titik terdekat dan proyeksinya 
        print("=============================================================")
        print("Koordinat titik terdekat: ", koordinat)
        project.projectionAfter3D(koordinatSorting, koordinat)
        print("=============================================================")

    print("")
    
    # Opsi untuk kembali mencari titik terdekat atau keluar dari program
    question = input("Apakah Anda ingin mencari titik terdekat lagi? (Y/N): ")
    if question == "Y" or question == "y":
        keluarProgram = False
    elif question == "N" or question == "n":
        keluarProgram = True

# Closing Splash
splash.closingSplash()