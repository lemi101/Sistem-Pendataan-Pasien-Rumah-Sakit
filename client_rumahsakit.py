import json, xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:6667')

try : 
	while(True) :
		print("Sistem Informasi Pasien")
		print("1. Masukkan data pasien")
		print("2. Lihat data pasien")
		print("3. Keluar")
		operasi = input("Pilih operasi : ")
		if operasi == "1" :
			print("Masukkan data pasien")
			nik = input("NIK : ")
			nama = input("Nama : ")
			alamat = input("Alamat : ")
			penyakit = input("Penyakit : ")

			pesan = proxy.add_pasien(nik, nama, alamat, penyakit)
			print(pesan)

		elif operasi == "2" :
			data = proxy.get_pasien()
			data = json.loads(data)

			print(data)

		else :
			print("Keluar dari program")
			break
    
except KeyboardInterrupt :
	print("Keluar dari program")