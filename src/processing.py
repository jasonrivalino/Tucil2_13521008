import math
import psutil
import platform

# Sorting untuk mengurutkan koordinat berdasarkan x menaik
def sortingX(listKoordinat):
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if listKoordinat[i][0] < listKoordinat[j][0]:
                listKoordinat[i], listKoordinat[j] = listKoordinat[j], listKoordinat[i]
    return listKoordinat

# Sorting untuk mengurutkan koordinat berdasarkan y menaik
def sortingY(listKoordinat):
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if listKoordinat[i][1] < listKoordinat[j][1]:
                listKoordinat[i], listKoordinat[j] = listKoordinat[j], listKoordinat[i]
    return listKoordinat

#inisialisasi variabel global
hitungEuclideanBF = 0

# Melakukan proses brute force untuk mencari jarak terdekat
def bruteForce(listKoordinat,dimensi):
    global hitungEuclideanBF
    jarak = []
    min = float("inf")
    for i in range (len(listKoordinat)):
        for j in range (len(listKoordinat)):
            if i != j:
                if dimensi == 1:
                    jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))))
                    hitungEuclideanBF += 1
                elif dimensi == 2:
                    jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                           (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))))
                    hitungEuclideanBF += 1
                elif dimensi == 3:
                    jarak.append(math.sqrt((pow((listKoordinat[j][0]-listKoordinat[i][0]),2))+
                                           (pow((listKoordinat[j][1]-listKoordinat[i][1]),2))+
                                           (pow((listKoordinat[j][2]-listKoordinat[i][2]),2))))
                    hitungEuclideanBF += 1
    for i in range (len(jarak)):
        if jarak[i] < min:
            min = jarak[i]
    return min

#inisialisasi variabel global
hitungEuclideanDC = 0

# Melakukan proses divide and conquer untuk mencari jarak terdekat
def divideAndConquer(listKoordinat, n, dimensi):
    global hitungEuclideanDC
    n = len(listKoordinat)
    jarak = 0
    # Basis 1
    if n == 2:
        if dimensi == 1:
            jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2)))
            hitungEuclideanDC += 1
            tempNearest = [listKoordinat[0], listKoordinat[1]]
            return jarak, tempNearest
        elif dimensi == 2:
            jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                              (pow((listKoordinat[1][1]-listKoordinat[0][1]),2)))
            hitungEuclideanDC += 1
            tempNearest = [listKoordinat[0], listKoordinat[1]]
            return jarak, tempNearest
        elif dimensi == 3:
            jarak = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                              (pow((listKoordinat[1][1]-listKoordinat[0][1]),2))+
                              (pow((listKoordinat[1][2]-listKoordinat[0][2]),2)))
            hitungEuclideanDC += 1
            tempNearest = [listKoordinat[0], listKoordinat[1]]
            return jarak, tempNearest
    # Basis 2
    elif n == 3:
        if dimensi == 1:
            jarak1 = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2)))
            jarak2 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[0][0]),2)))
            jarak3 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[1][0]),2)))
            if jarak1 < jarak2 and jarak1 < jarak3:
                hitungEuclideanDC += 1
                jarak = jarak1
                tempNearest = [listKoordinat[0], listKoordinat[1]]
            elif jarak2 < jarak1 and jarak2 < jarak3:
                hitungEuclideanDC += 1
                jarak = jarak2
                tempNearest = [listKoordinat[0], listKoordinat[2]]
            else:
                hitungEuclideanDC += 1
                jarak = jarak3
                tempNearest = [listKoordinat[1], listKoordinat[2]]
            return jarak, tempNearest
        elif dimensi == 2:
            jarak1 = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                               (pow((listKoordinat[1][1]-listKoordinat[0][1]),2)))
            jarak2 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[0][0]),2))+
                               (pow((listKoordinat[2][1]-listKoordinat[0][1]),2)))
            jarak3 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[1][0]),2))+
                               (pow((listKoordinat[2][1]-listKoordinat[1][1]),2)))
            if jarak1 < jarak2 and jarak1 < jarak3:
                hitungEuclideanDC += 1
                jarak = jarak1
                tempNearest = [listKoordinat[0], listKoordinat[1]]
            elif jarak2 < jarak1 and jarak2 < jarak3:
                hitungEuclideanDC += 1
                jarak = jarak2
                tempNearest = [listKoordinat[0], listKoordinat[2]]
            else:
                hitungEuclideanDC += 1
                jarak = jarak3
                tempNearest = [listKoordinat[1], listKoordinat[2]]
            return jarak, tempNearest
        elif dimensi == 3:
            jarak1 = math.sqrt((pow((listKoordinat[1][0]-listKoordinat[0][0]),2))+
                               (pow((listKoordinat[1][1]-listKoordinat[0][1]),2))+
                               (pow((listKoordinat[1][2]-listKoordinat[0][2]),2)))
            jarak2 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[0][0]),2))+
                               (pow((listKoordinat[2][1]-listKoordinat[0][1]),2))+
                               (pow((listKoordinat[2][2]-listKoordinat[0][2]),2)))
            jarak3 = math.sqrt((pow((listKoordinat[2][0]-listKoordinat[1][0]),2))+
                               (pow((listKoordinat[2][1]-listKoordinat[1][1]),2))+
                               (pow((listKoordinat[2][2]-listKoordinat[1][2]),2)))
            if jarak1 < jarak2 and jarak1 < jarak3:
                jarak = jarak1
                tempNearest = [listKoordinat[0], listKoordinat[1]]
                # print(tempNearest)
                hitungEuclideanDC += 1
            elif jarak2 < jarak1 and jarak2 < jarak3:
                jarak = jarak2
                tempNearest = [listKoordinat[0], listKoordinat[2]]
                # print(tempNearest)
                hitungEuclideanDC += 1
            else:
                jarak = jarak3
                tempNearest = [listKoordinat[1], listKoordinat[2]]
                # print(tempNearest)
                hitungEuclideanDC += 1
            return jarak, tempNearest
    # Rekurens
    else:
        # Membagi data menjadi 2 bagian
        middle = n//2
        left_area = []
        right_area = []
        for i in range (middle):
            left_area.append(listKoordinat[i])
        for i in range (middle, n):
            right_area.append(listKoordinat[i])

        # Mencari jarak terdekat di bagian kiri dan kanan secara rekursif
        jarak1, koordinat1 = divideAndConquer(left_area, n, dimensi)
        hitungEuclideanDC += 1
        jarak2, koordinat2 = divideAndConquer(right_area, n, dimensi)
        hitungEuclideanDC += 1

        # Mencari koordinat dua titik terdekat
        if jarak1 <= jarak2:
            jarak = jarak1
            tempNearest = koordinat1
        elif jarak1 > jarak2:
            jarak = jarak2
            tempNearest = koordinat2

        # Mencari jarak terdekat di antara kiri dan kanan jika jaraknya kurang dari strip (cek kondisi di tengah garis batas)
        strip = []
        for i in range (n):
            if abs(listKoordinat[i][0] - listKoordinat[middle][0]) < jarak:
                strip.append(listKoordinat[i])

        # Mencari jarak terdekat di antara titik-titik yang ada di dalam strip
        if dimensi == 1:
            for i in range (len(strip)):
                for j in range (i+1, len(strip)):
                    if (strip[j][0] - strip[i][0]) >= jarak and (strip[j][1] - strip[i][1]) >= jarak:
                        break
                    newJarak = math.sqrt((pow((strip[j][0]-strip[i][0]),2)))
                    if newJarak < jarak:
                        jarak = newJarak
                        tempNearest = [strip[i], strip[j]]
                        hitungEuclideanDC += 1
            return jarak, tempNearest
        
        elif dimensi == 2 or dimensi == 3:
            # Sorting strip berdasarkan koordinat y menaik
            strip_sorted = sortingY(strip)

            # Mencari jarak terdekat di antara titik-titik yang ada di dalam strip
            for i in range (len(strip_sorted)):
                for j in range (i+1, len(strip_sorted)):
                    if (strip_sorted[j][0] - strip_sorted[i][0]) >= jarak and (strip_sorted[j][1] - strip_sorted[i][1]) >= jarak:
                        break
                    if dimensi == 2:
                        newJarak = math.sqrt((pow((strip_sorted[j][0]-strip_sorted[i][0]),2))+
                                             (pow((strip_sorted[j][1]-strip_sorted[i][1]),2)))
                    elif dimensi == 3:
                        newJarak = math.sqrt((pow((strip_sorted[j][0]-strip_sorted[i][0]),2))+
                                             (pow((strip_sorted[j][1]-strip_sorted[i][1]),2))+
                                             (pow((strip_sorted[j][2]-strip_sorted[i][2]),2)))
                    if newJarak < jarak:
                        jarak = newJarak
                        tempNearest = [strip_sorted[i], strip_sorted[j]]
                        hitungEuclideanDC += 1
            return jarak, tempNearest

# Menampilkan spesifikasi laptop untuk running program
def spekLaptop():
    print("==============================================================")
    print("SPESIFIKASI LAPTOP UNTUK RUNNING PROGRAM")
    print("--------------------------------------------------------------")
    print("Processor:", platform.processor())
    print("Operating System:", platform.platform())
    print("Machine:", platform.machine())
    total_ram = psutil.virtual_memory().total / (1024.0 **3)
    print("RAM:",total_ram, "GB")
    print("==============================================================")