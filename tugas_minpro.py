#Nama : Otniel Putra Wardana
#NIM  : 2509116081
#Tugas Minpro Sistem Reservasi Lapangan Bulu Tangkis

#Create

Nama = input("masukan Nama Anda: ")
Tanggal_reservasi = str(input("masukan tanggal reservasi (HH/BB): "))
jam_mulai = str(input("masukan jam mulai reservasi (JJ:MM): "))
jam_selesai = str(input("masukan jam selesai reservasi (JJ:MM): "))

data_list = [Nama, Tanggal_reservasi, jam_mulai, jam_selesai]
data_tuple = (Nama, Tanggal_reservasi, jam_mulai, jam_selesai)

#Read

print ("   ")
print ("### data berhasil dimasukan ###")
print ("   ")
print ("==", data_list, "ini adalah data reservasi anda untuk sekarang.==")
print ("== Silahkan mengubahnya jika terjadi kesalahan dalam menginput data ==")
print ("   ")
print ("== silahkan ketik angka yang ingin anda lakukan sekarang ==")
print ("   ")
print ("apa yang ingin anda lakukan?")
print ("0. konfirmasi pesanan reservasi lapangan")
print ("1. mengubah jam atau waktu reservasi")
print ("   ")
pilihan = (int(input("masukan angka no 0-1: ")))

if pilihan == 0:
    print ("reservasi atas pesanan", data_list, "telah terverifikasi")

#Update

elif pilihan == 1:
    a = (int(input("apa yang ingin diubah? (1 untuk tanggal reservasi, 2 untuk jam mulainya, 3 untuk jam selesainya): ")))
    if a == 1:
        a = str(input("masukan tanggal yang ingin diubah:" ))
        data_list[1] = a
        print ("tanggal telah diubah. data yang awalnya dari", data_tuple, "berikut data lengkap yang telah di update.", data_list)
    elif a == 2:
        a = str(input("masukan jam mulai yang ingin diubah: "))
        data_list[2] = a
        print ("jam mulai telah diubah. data yang awalnya dari", data_tuple, "berikut data lengkap yang telah di update.", data_list)
    elif a == 3:
        a = str(input("masukan jam selesai yang ingin diubah: "))
        data_list[3] = a
        print ("jam selesai telah diubah. data yang awalnya dari", data_tuple, "berikut data lengkap yang telah di update.", data_list)
    else:
        print ("masukan dengan opsi yg benar (1/2/3)")