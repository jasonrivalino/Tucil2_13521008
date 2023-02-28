# Tugas Kecil 2 Mata Kuliah Strategi Algoritma IF2211
> Tugas Kecil 2: Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer


## Creator
Jason Rivalino - 13521008


## Table of Contents
* [Deskripsi Singkat](#deskripsi-singkat)
* [Struktur File](#struktur-file)
* [Requirements](#requirements)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Progress Report](#progress-report)
* [Acknowledgements](#acknowledgements)


## Deskripsi Singkat 
Algoritma Divide and Conquer merupakan algoritma yang menyelesaikan permasalahan dengan membagi permasalahan ke dalam bagian-bagian yang lebih kecil, lalu diselesaikan dan disatukan kembali. Salah satu contoh permasalahan yang dapat diselesaikan dengan algoritma ini adalah permasalahan pencarian sepasang titik terdekat (Closest Pair). Persoalan tersebut dirumuskan untuk titik pada bidang datar (2D). Pada Tugas Kecil 2 kali ini, tugas yang diberikan adalah untuk mengembangkan algoritma mencari sepasang titik terdekat pada bidang 3D. Misalkan terdapat n buah titik pada ruang 3D. Setiap titik P di dalam ruang dinyatakan dengan koordinat P = (x, y, z). Carilah sepasang titik yang mempunyai jarak terdekat satu sama lain.


## Struktur File
```bash
📦Tucil2_13521008
 ┣ 📂bin
 ┣ 📂doc
 ┃ ┗ 📜Tucil2_K3_13521008_Jason Rivalino.pdf
 ┣ 📂src
 ┃ ┣ 📜inputting.py
 ┃ ┣ 📜main.py
 ┃ ┣ 📜processing.py
 ┃ ┣ 📜projection.py
 ┃ ┗ 📜splash.py
 ┣ 📂test
 ┃ ┣ 📜test1dimensi(1000).png
 ┃ ┣ 📜test1dimensi(20).png
 ┃ ┣ 📜test1dimensi(50).png
 ┃ ┣ 📜test2dimensi(1000).png
 ┃ ┣ 📜test2dimensi(20).png
 ┃ ┣ 📜test2dimensi(50).png
 ┃ ┣ 📜test3dimensi(1000).png
 ┃ ┣ 📜test3dimensi(20).png
 ┃ ┗ 📜test3dimensi(50).png
 ┗ 📜README.md
 ```


## Requirements
1. Bahasa Pemrograman Python (sudah dilengkapi dengan library numpy, matplotlib, dan psutil)

Instalasi pada terminal:
```bash
pip install numpy
pip install matplotlib
pip install psutil
```

2. Aplikasi Code Runner (Rekomendasi: Visual Studio Code)


## Cara Menjalankan Program
Langkah-langkah proses setup program adalah sebagai berikut:
1. Clone Repository Github ini
2. Run program dengan mengetikkan `py src/Main.py` pada terminal pada directory yang sesuai dengan directory lokasi clone program 

## Progress Report
| No | Poin | Ya | Tidak
| :---: | --- | :---: | :---: |
| 1. | Program berhasil dikompilasi tanpa ada kesalahan | ✓ |  |
| 2. | Program berhasil running | ✓ |  |
| 3. | Program dapat menerima masukan dan dan menuliskan luaran | ✓ |  |
| 4. | Luaran program sudah benar (solusi closest pair benar) | ✓ |  |
| 5. | Bonus 1: Penggambaran semua titik di bidang 3D, sepasang titik yang terdekat ditunjukkan dengan warna yang berbeda | ✓ |  |
| 6. | Bonus 2: Generalisasi program sehingga dapat mencari sepasang titik terdekat untuk kumpulan vektor berdimensi n | ✓ |  |

Note: untuk bonus 2, implementasi yang dibuat hanya bisa untuk mencari sepasang titik terdekat dalam bidang 1-3 dimensi

## Acknowledgements
- Tuhan Yang Maha Esa
- Dosen Mata Kuliah yaitu Pak Rinaldi (K1), Bu Ulfa (K2), dan Pak Rila (K3)
- Kakak-Kakak Asisten Mata Kuliah Strategi Algoritma IF2211
