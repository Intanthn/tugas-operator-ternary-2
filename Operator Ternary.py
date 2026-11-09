print(" DATA PASIEN RUMAH SAKIT ")

penyakit = {
    "1": ("Demam Berdarah", "Penyakit Infeksi", "3-7 hari"),
    "2": ("Tipes", "Penyakit Infeksi", "5-7 hari"),
    "3": ("Demam", "Gangguan Kesehatan Umum", "1-2 hari"),
    "4": ("Pneumonia", "Gangguan Pernapasan", "5-10 hari"),
    "5": ("Diare", "Gangguan Pencernaan", "2-3 hari"),
    "6": ("Asma", "Gangguan Pernapasan", "2-5 hari"),
    "7": ("Anemia", "Gangguan Darah", "2-4 hari"),
    "8": ("Infeksi Paru", "Penyakit Infeksi", "5-10 hari"),
    "9": ("Gastritis", "Gangguan Pencernaan", "1-3 hari"),
    "10": ("Malaria", "Penyakit Infeksi", "3-7 hari")
}

nama = input("Masukkan nama pasien: ")

print("\nPilih penyakit:")
for nomor, data in penyakit.items():
    print(nomor + ".", data[0])

pilihan = input("Masukkan nomor penyakit: ")

if pilihan in penyakit:
    data = penyakit[pilihan]

    kategori = data[1]
    opname = data[2]

    status = "Terdaftar" if pilihan in penyakit else "Tidak Terdaftar"

    print("\n HASIL DATA PASIEN ")
    print("Nama:", nama)
    print("Penyakit:", data[0])
    print("Kategori:", kategori)
    print("Perkiraan Lama Opname:", opname)
    print("Status:", status)

else:
    print("Penyakit tidak tersedia!")