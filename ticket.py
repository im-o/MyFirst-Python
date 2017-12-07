#!/usr/bin/python
#author rival
#python 3.5

print("\n\t[------- APLIKASI TIKET WISATA -------]")
def lTiket():
    print ("\n\t[ Berikut Jenis-Jenis dan Harga Tiket ]\n")
    print ("+------------------------+")
    print ("|   JENIS   |   HARGA    |")
    print ("+------------------------+")
    print ("| siswa     : Rp 150.000 |")
    print ("| mahasiswa : Rp 200.000 |")
    print ("| umum      : Rp 300.000 |")
    print ("+------------------------+\n")
    
def jTiket():
    if ((jnsTiket=="siswa")|(jnsTiket=="SISWA")):
        print ("Harga Tiket 150.000/org")
    elif ((jnsTiket=="mahasiswa")|(jnsTiket=="MAHASISWA")):
        print ("Harga Tiket 200.000/org")
    elif ((jnsTiket=="umum")|(jnsTiket=="UMUM")):
        print ("Harga Tiket 300.000/org\n")
    else:
        print("Input Tidak Tersedia")
        exit()
        
def tiketGratis():
    ttlTiket = 0
    if ((jmlTiket >=10)&(jmlTiket <=20)):
        print("  ANDA MENDAPATKAN TIKET GRATIS : 2")
        ttlTiket = jmlTiket+2
        print ("  TOTAL TIKET : ",ttlTiket)
    elif ((jmlTiket >=21)&(jmlTiket <=30)):
        print("  ANDA MENDAPATKAN TIKET GRATIS : 4")
        ttlTiket = jmlTiket+4
        print ("  TOTAL TIKET : ",ttlTiket)
    elif ((jmlTiket >=31)&(jmlTiket <=40)):
        print("  ANDA MENDAPATKAN TIKET GRATIS : 6")
        ttlTiket = jmlTiket+6
        print ("  TOTAL TIKET : ",ttlTiket)
    elif ((jmlTiket >=41)&(jmlTiket <=50)):
        print("  ANDA MENDAPATKAN TIKET GRATIS : 9")
        ttlTiket = jmlTiket+9
        print ("  TOTAL TIKET : ",ttlTiket)
    else:
        print("  TIDAK ADA TIKET GRATIS")
        print("  TOTAL TIKET : ",jmlTiket)
def tBayar():
    JUMLAH=0
    if ((jnsTiket=="siswa")|(jnsTiket=="SISWA")):
        JUMLAH = jmlTiket*150000
        print ("  TOTAL BAYAR : Rp",JUMLAH)
    elif ((jnsTiket=="mahasiswa")|(jnsTiket=="MAHASISWA")):
        JUMLAH = jmlTiket*200000
        print ("  TOTAL BAYAR : Rp",JUMLAH)
    elif ((jnsTiket=="umum")|(jnsTiket=="UMUM")):
        JUMLAH = jmlTiket*300000
        print ("  TOTAL BAYAR : Rp",JUMLAH)
    else:
        print("Tidak Tersedia")
        exit()
lagi = "y"
while ((lagi =="y")|(lagi =="Y")):
    nPelanggan = input("\nMasukkan nama anda : ")
    lTiket()
    jnsTiket = input("\nInput Jenis Tiket : ")
    jTiket()
    jmlTiket = int(input("\nJumlah Tiket : "))
    print ("\n+---------------------------------------------+")
    print ("  NAMA PELANGGAN YANG MEMESAN : ",nPelanggan)
    tiketGratis()
    tBayar()
    print ("+---------------------------------------------+")
    lagi = input("\nMasih ada lagi data ? (y/n) : ")
print ("\nTerimakasih")
