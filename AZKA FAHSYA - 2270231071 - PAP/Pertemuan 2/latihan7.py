#OPERATOR ARITMATIKA

#Penjumlahan
print(13 + 2)
apel = 7
jeruk = 9
buah = apel + jeruk #
print(buah)

#Pengurangan
hutang = 10000
bayar = 5000
sisaHutang = hutang - bayar
print("Sisa hutang Anda adalah ", sisaHutang)

#Perkalian
panjang = 15
lebar = 8
luas = panjang * lebar
print(luas)

#Pembagian
kue = 16
anak = 4
kuePerAnak = kue / anak
print("Setiap anak akan mendapatkan bagian kue sebanyak ", kuePerAnak)

#Sisa Bagi / Modulus
bilangan1 = 14
bilangan2 = 5
hasil = bilangan1 % bilangan2
print("Sisa bagi dari bilangan ", bilangan1, " dan ", bilangan2, " adalah ", hasil)

#Pangkat
bilangan3 = 8
bilangan4 = 2
hasilPangkat = bilangan3 ** bilangan4
print(hasilPangkat)

#Pembagian Bulat
print(10//3)
#10 dibagi 3 adalah 3.3333. Karena dibulatkan maka akan menghasilkan nilai 3
print('"Halo, apa kabar?"')

print("'Halo, apa kabar?'") 
print("ini adalah hari jum'at")


# 2. Menggunakan tanda \


# membuat tanda ' menjadi string 
print('mari shalat jum\'at') 
print('g\'day, isn\'t it?')


# backlash 
print("C:\\user\\Ucup")


# tab

print("ucup\t\t\totong, semakin jauhan")


# backspace

print("ucup \botong, jadi deketan")


# newline

print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows


# 3. String literal atau raw


# hati-hati

print('C:\new folder') # akan salah pathnya


# menggunakan raw string 
print(r'C:\new folder')


# multiline literal string 
print("""
Nama : Ucup Kelas : 3 SD """)


# multiline literal string dan RAW 
print(r"""
Nama : Ucup

Kelas : 3 SD\new normal Website : www.ucup.com/newID """)
