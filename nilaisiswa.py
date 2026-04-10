# data mahasiswa
nim = ["231001", "231002", "231003", "231004"]
nama = ["Andi", "Budi", "Citra", "Dina"]

mk1 = [80, 90, 70, 88]
mk2 = [75, 85, 72, 90]
mk3 = [70, 88, 68, 84]
mk4 = [85, 92, 74, 86]

rata = []

# menghitung rata-rata tiap mahasiswa
for i in range(len(nim)):
    r = (mk1[i] + mk2[i] + mk3[i] + mk4[i]) / 4
    rata.append(r)

# mencari mahasiswa paling pintar
max_rata = max(rata)
index = rata.index(max_rata)

# menghitung rata-rata tiap mata kuliah
rata_mk1 = sum(mk1) / len(mk1)
rata_mk2 = sum(mk2) / len(mk2)
rata_mk3 = sum(mk3) / len(mk3)
rata_mk4 = sum(mk4) / len(mk4)

# mencari mata kuliah dengan rata-rata terkecil
mk = [rata_mk1, rata_mk2, rata_mk3, rata_mk4]
mk_terkecil = min(mk)
posisi = mk.index(mk_terkecil) + 1

# output

print("\nMahasiswa paling pintar:")
print("NIM :", nim[index])
print("Nama:", nama[index])
print("Rata-rata:", max_rata)

print("\nMata kuliah dengan rata-rata paling kecil: MK", posisi)