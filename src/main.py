import inputting as inp
import processing as process
import projection as project
import splash as splash
import time

# Fungsi utama untuk mencari jarak terdekat antar titik dan menampilkan hasilnya
def mainSolvingProblem(dimensi, koordinatSorting):
    project.projectionBefore(koordinatSorting, dimensi)
        
    print("")

    process.spekLaptop()

    print("")

    # Melakukan proses brute force
    start_bf_time = time.time()
    jarak = process.bruteForce(koordinatSorting, dimensi)
    stop_bf_time = time.time()

    # Menampilkan hasil dengan Algoritma Brute Force
    print("==============================================================")
    print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
    print("--------------------------------------------------------------")
    print("Jarak terdekat antar titik:", jarak)
    print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanBF)
    print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
    print("==============================================================")

    print("")

    # Melakukan proses divide and conquer
    start_bf_time = time.time()
    jarak, koordinat = process.divideAndConquer(koordinatSorting, len(koordinatSorting), dimensi)
    stop_bf_time = time.time()

    # Menampilkan hasil dengan Algoritma Divide and Conquer
    print("==============================================================")
    print("MENCARI DENGAN ALGORITMA DIVIDE AND CONQUER")
    print("--------------------------------------------------------------")
    print("Jarak terdekat antar titik:", jarak)
    print("Banyaknya perhitungan operasi Euclidean:", process.hitungEuclideanDC)
    print("Waktu menjalankan program: %.7s detik" % (stop_bf_time - start_bf_time))
    print("==============================================================")

    print("")

    # Menampilkan koordinat titik terdekat dan proyeksinya
    print("==============================================================")
    print("Koordinat titik terdekat: ", koordinat)
    project.projectionAfter(koordinatSorting, koordinat, dimensi)


# MAIN PROGRAM

# Opening Splash
splash.openingSplash()

# Inisialisasi variabel
process.hitungEuclideanBF = 0
process.hitungEuclideanDC = 0
n = 0

# Input jumlah titik
n = inp.inputTitik(n)

# Input dimensi
print("")
dimensi = inp.inputDimension(n)

# Input koordinat
listKoordinat = inp.inputKoordinat(n, dimensi)

# Melakukan proses sorting
koordinatSorting = process.sortingX(listKoordinat)
    
# Memanggil fungsi utama untuk mencari jarak terdekat antar titik dan menampilkan hasilnya
mainSolvingProblem(dimensi, koordinatSorting)

print("")

# Closing Splash
splash.closingSplash()