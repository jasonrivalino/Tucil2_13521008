import function as fun
import time

# Main program
n = 0
n = fun.inputTitik(n)
# print(n)
listKoordinat = fun.inputKoordinatTigaDimensi(n)
# print("")
# print("Titik-titik yang didapat adalah: ")
# print(listKoordinat)
# print("")
# print("List koordinat setelah disorting: ")
koordinatSorting = fun.sorting(listKoordinat)
# print(koordinatSorting)
fun.projectionBefore(koordinatSorting)
print("")
start_time = time.time()
jarak = fun.bruteForce(koordinatSorting)
stop_time = time.time()

print("MENCARI DENGAN ALGORITMA BRUTE FORCE")
print("Jarak terdekat antar titik:", min(jarak))
print("Waktu menjalankan program: %.7s detik" % (stop_time - start_time))