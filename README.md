#### Latihan1
	
	Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda
	import math
	def a(x):
	return x**2
	def b(x, y):
	return math.sqrt(x**2 + y**2)
	def c(*args):
	return sum(args)/len(args)
	def d(s):
	return "".join(set(s))


![1.png](/gambar2/1.png)
![1.png](/gambar1/1.png)



#### Syntax pada latihan1

		# -*- coding: utf-8 -*-
		"""
		Spyder Editor

		This is a temporary script file.
		"""

		#def a(x):
		#return x**2
		a = (lambda x: x ** 2)
		print(a(10))

		#def b(x, y):
		#return math.sqrt(x**2 + y**2)
		b = (lambda x,y: x**2 + y**2)
		print(b(4,8))

		#def c(*args):
		#return sum(args)/len(args)
		c = (lambda *args: sum(args)/ len(args))
		print(c(4))

		#def d(s):
		#return "".join(set(s))
		d = (lambda s: "".join(set(s)))
		print(d("vwxyz"))

	


#### Output pada latihan1

![2.png](/gambar2/2.png)


### Tugas Praktikum

	Buat program sederhana dengan mengaplikasikan penggunaan fungsi
	yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
	• Fungsi tambah() untuk menambah data
	• Fungsi tapilkan() untuk menampilkan data
	• Fungsi hapus(nama) untuk menghapus data berdasarkan nama
	• Fungsi ubah(nama) untuk mengubah data berdasarkan nama
	• Buat flowchart dan penjelasan programnya pada README.md.
	• Commit dan push repository ke github.

![1.png](/gambar1/1.png)

![2.png](/gambar1/2.png)

![3.png](/gambar1/3.png)

#### Syntax Tugas Praktikum


		# -*- coding: utf-8 -*-
		"""
		Created on Thu Dec  3 08:55:47 2020

		@author: BLACK
		"""

		data = {}

		def tambah():
    			print("Tambah Data")
    			nama = input("Nama\t\t: ")
    			nim = int(input("NIM\t\t\t: "))
    			tugas = int(input("NIlai Tugas\t: "))
    			uts = int(input("Nilai UTS\t: "))
    			uas = int(input("Nilai UAS\t: "))
    			nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    			data[nama] = nim, tugas, uts, uas, nilaiakhir


		def tampilkan():
    			if data.items():
        			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        			print("_______________________________________________________________________________________")
       				print("|  No  |      NIM      |      NAMA         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
        			print("|______|_______________|___________________|____________|_________|_________|________|__")
        			i = 0
        			for a in data.items():
            				i += 1
            				print(f"| {i:4} | {a[0]:13s} | {a[1][0]:17} | {a[1][1]:10d} | {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    			else:
        			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        			print("_______________________________________________________________________________________")
        			print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        			print("_______________________________________________________________________________________")
        			print("|      |               |             Tidak Ada Data         |         |                |")
    			print("____________________________________________________________________________________________")


		def hapus():
    			print("Hapus Data Nilai Mahasiswa")
    			nama = input(" Masukan Nama\t:")
    			if nama in data.keys():
        			del data[nama]
        			print()
        			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        			print("===| BERHASIL MENGHAPUS DATA |===")
        			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    			else:
        			print("Data {0} tidak ada".format(nama))


		def ubah():
    			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    			print("===| Edit Data Nilai Mahasiswa |===")
    			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    			nama = input("Masukan Nama\t\t: ")
    			print("___________________________________")
    			if nama in data.keys():
        			nim = input("NIM baru\t\t\t: ")
        			tugas = int(input("Nilai Tugas Baru\t: "))
        			uts = int(input("Nilai UTS Baru\t\t: "))
        			uas = int(input("Nilai UAS Baru\t\t: "))
        			nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        			data[nama] = nim, tugas, uts, uas, nilaiakhir
        			print()
        			print("<><><><><><><><><><><><><><><><>")
        			print("====| BERHASIL MENGUBAH DATA |====")
        			print("<><><><><><><><><><><><><><><><>")
    			else:
        			print("Data nilai {0} tidak ada ".format(nama))


		while True:
    			print("")
    			print("|_<><><><><><><><><><><><><><><><><>_|")
    			print("|~~~~~~~~| DATA MAHASISWA |~~~~~~~~~~|")
    			print("|_<><><><><><><><><><><><><><><><><>_|")
    			x = input("1.| Lihat Data \n2.| Tambah Data \n3.| Ubah Data \n4.| Hapus Data \n0.| Keluar Aplikasi \nPilih menu : ")
    			if x.lower() == "1":
        			tampilkan()
    			elif x.lower() == "2":
        			tambah()
    			elif x.lower() == "3":
        			ubah()
    			elif x.lower() == "4":
        			hapus()
    			elif x.lower() == "0":
        			print()
        				print("<><><><><><><><><><><><><><><><>")
        				print("====== KELUAR DARI PROGRAM ======")
        				print("<><><><><><><><><><><><><><><><>")
        				break

    			else:
        			print()
        			print("<><><><><><><><><><><><><><><><>")
        			print("== Pilihan Anda Tidak Tersedia ==")
        			print("== Pilihlah Menu Yang Tersedia ==")
        			print("<><><><><><><><><><><><><><><><>")



Ouput untuk Lihat Data

![4.png](/gambar1/4.png)

Ouput untuk Tambah Data

![5.png](/gambar1/5.png)

Ouput untuk Ubah Data

![6.png](/gambar1/6.png)

Output untuk Hapus Data

![7.png](/gambar1/7.png)

Output untuk Keluar Aplikasi

![8.png](/gambar1/8.png)


























































































































