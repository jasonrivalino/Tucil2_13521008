import inputting as inp
import processing as process
import projection as project
import splash as splash
import time

# Fungsi utama untuk mencari jarak terdekat antar titik dan menampilkan hasilnya
def mainSolvingProblem(dimensi, koordinatSorting):
    if dimensi == 1:
        project.projectionBefore1D(koordinatSorting)
    elif dimensi == 2:
        project.projectionBefore2D(koordinatSorting)
    elif dimensi == 3:
        project.projectionBefore3D(koordinatSorting)
        
    print("")

    # Melakukan proses brute force
    start_bf_time = time.time()
    if dimensi == 1:
        jarak = process.bruteForce1D(koordinatSorting)
    elif dimensi == 2:
        jarak = process.bruteForce2D(koordinatSorting)
    elif dimensi == 3:
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
    if dimensi == 1:
        jarak, koordinat = process.divideAndConquer1D(koordinatSorting, len(koordinatSorting), 3)
    elif dimensi == 2:
        jarak, koordinat = process.divideAndConquer2D(koordinatSorting, len(koordinatSorting), 3)
    elif dimensi == 3:
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
    if dimensi == 1:
        project.projectionAfter1D(koordinatSorting, koordinat)
    elif dimensi == 2:
        project.projectionAfter2D(koordinatSorting, koordinat)
    elif dimensi == 3:
        project.projectionAfter3D(koordinatSorting, koordinat)
    print("=============================================================")

# MAIN PROGRAM

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
    if dimensi == 1:
        listKoordinat = inp.inputKoordinatSatuDimensi(n)
    elif dimensi == 2:
        listKoordinat = inp.inputKoordinatDuaDimensi(n)
    elif dimensi == 3:
        listKoordinat = inp.inputKoordinatTigaDimensi(n)

    # Melakukan proses sorting
    koordinatSorting = process.sortingX(listKoordinat)
    
    mainSolvingProblem(dimensi, koordinatSorting)

    print("")
    
    # Opsi untuk kembali mencari titik terdekat atau keluar dari program
    question = input("Apakah Anda ingin mencari titik terdekat lagi? (Y/N): ")
    if question == "Y" or question == "y":
        keluarProgram = False
    elif question == "N" or question == "n":
        keluarProgram = True

# Closing Splash
splash.closingSplash()