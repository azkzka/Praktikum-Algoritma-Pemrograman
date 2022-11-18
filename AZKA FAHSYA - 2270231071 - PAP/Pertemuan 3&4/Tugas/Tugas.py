#by; @azkzka_

def menu() :
    print('-----------------------------------------')
    print('           BILLION VAPE STORE')
    print('               by : azka')
    print('-----------------------------------------')
    print('Kode Barang | Nama Barang |     Harga')
    print('    PD      |     POD     |  Rp. 100.000')
    print('    MD      |     MOD     |  Rp. 350.000')
    print('    IO      |     AIO     |  Rp. 230.000')
    print('-----------------------------------------')

menu()
nama = input('Masukan Nama Pembeli : ')
telp = input('Masukan Nomer HP : ')
alamat = input('Masukan Alamat : ')
def garis():
    print('-----------------------------------------')
garis()
jumlah_beli = int(input('Masukan Jumlah Transaksi : '))
kode_barang=[]
nama_barang=[]
masukan_jumlah=[]
total_belanja=[]
uang_bayar=[]
uang_kembali=[]
harga=[]
jumlah=[]
i = 0
while i < jumlah_beli:
    print('Data Ke -',i+1)

    kode_barang.append(input('Masukan Kode Barang : '))
    masukan_jumlah.append(int(input('Masukan Jumlah Beli : ')))
    if kode_barang[i] == 'PD' :
        nama_barang.append('POD')
        harga.append('100000')
        jumlah.append(masukan_jumlah[i]*int(100000))
    elif kode_barang[i] == 'MD' :
        nama_barang.append('MOD')
        harga.append('350000')
        jumlah.append(masukan_jumlah[i]*int(350000))
    elif kode_barang[i] == 'IO' :
        nama_barang.append('AIO')
        harga.append('230000')
        jumlah.append(masukan_jumlah[i]*int(230000))
    else :
        nama_barang.append('Kode Salah')
        harga.append('0')
        jumlah.append(masukan_jumlah[i]*int('0'))
    i = i+1
garis()
print()
print()
print()
print('            BILLION VAPE STORE')
print('                by : azka')
print()
print('Nama Pembeli :',nama )
print('No HP  :',telp)
print('Alamat :',alamat)

def menu() :
    print('-----------------------------------------')
    print('No | Nama Barang | Harga | Qty | Subtotal')
    print('-----------------------------------------')
menu()
total_belanjaan=0
a = 0
while a<jumlah_beli:
    total_belanjaan = total_belanjaan + jumlah[a]
    print (' %i       %s      %s    %i     %i'%(a+1, nama_barang[a], harga[a], masukan_jumlah[a], jumlah[a]))
    a = a+1
garis()
print('                        Total Rp.',total_belanjaan)
bayar = int(input('Uang Pembayaran : Rp. '))
uang_kembali = bayar-total_belanjaan
print('Uang Kembali    : Rp.',uang_kembali)
garis()
print('              TERIMA KASIH')