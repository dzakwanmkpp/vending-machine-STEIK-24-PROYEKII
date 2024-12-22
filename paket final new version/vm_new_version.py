# Program Vending Machine (Tugas Besar)
# Kelompok 15 K28 Computational Thinking
# 17 November 2024

# Kamus
# daftar_barang (arr) adalah lit daftar barang yang dijual
# harga_barang (arr) adalah list harga setiap daftar barang
# stok (arr) adalah list ketersediaan stok barang
# nutrisi (arr) adalah list informasi nutrisi barang
# menudipilih (int) adalah inputan pengguna untuk pilihan menu
# sibarang (int) adalah kode barang yang dipilih pengguna
# idbarangdipilih (int) adalah kode inputan pengguna untuk barang yang mau dibeli
# id_barang (int) adalah kode inputan pengguna untuk info nutrisi yang ingin dilihat
# jumlah_pembelian (int) adalah jumlah barang yang ingin dibeli pengguna
# transaksi (int) adalah jumlah transaksi yang harus dibayar pengguna
# nilai_uang (arr) adalah list nominal uang yang dapat digunakan pengguna untuk bertransaksi
# sisa_bayar (arr) adalah jumlah sisa transaksi yang harus dibayar pengguna jika memiliki kembalian
# x_masuk (int) adalah nominal uang yang dimasukkan pengguna
# borong_ngga (int) adalah kode pilihan pengguna untuk memborong atau tidak memborong barang

#TAMBAHAN VARIABEL PADA VERSI BARU
# terjual menyatakan jumlah item barang tersebut sudah terjual berapa banyak

import colorama
from colorama import Fore, Style
from datetime import datetime
from pustaka_tambahan import *

print(Fore.CYAN ,"\n-----------------------------------------------------------------------------------------------------------------------------")
print("                                                 STEI-K 2024 VENDING MACHINE")
print("-----------------------------------------------------------------------------------------------------------------------------")
print(Fore.WHITE)

#baca data dari file : data_aplikasi.csv
f = open("data_aplikasi.csv", "r")
daftar_barang =[]
harga_barang =[]
stok =[]
terjual = []
nutrisi = []
expired_date = []
for baris in f:
    #print(baris)
    data = baris.split(",")
    daftar_barang.append(data[0])
    harga_barang.append(int(data[1]))
    stok.append(int(data[2]))
    terjual.append(int(data[3])) #<--------untuk terjual
    expired_date.append(data[4].strip()) #<--------untuk expired date
    nutrisi.append(data[5])
f.close()

#baca data member dari file : data_member.csv
f = open("data_member.csv", "r")
daftarObjekMember =[]
for baris in f:
    #print(baris)
    data = baris.split(",")
    #print(data)
    #dari terdepan: username, notelp, poin, transaksi
    memberData = KelasMember(data[0],data[1],int(data[2]),int(data[3]))
    daftarObjekMember.append(memberData)
f.close()


#menampilkan data barang
print("DAFTAR BARANG:")
N = len(daftar_barang)
print("----------------------------------------")
print(" NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
print("----------------------------------------")
for i in range(N):
    print(" %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
print("----------------------------------------")

#menampilkan menu aplikasi
print()
print("PILIHAN MENU\n(khusus pilihan 3 hanya bisa dilakukan jika anda Admin): ")
print("\t-------------------------------------------------------------------------------------------------------")
print("\t          1. Membeli        |       2. Info Nutrisi       |    3. Manajemen Data   |     4. Keluar")
print("\t          Menu Baru:")
print("\t                     5. Membership (daftar gratis dan dapatkan poin dari setiap transaksimu)")
print("\t-------------------------------------------------------------------------------------------------------")
print("\n                                         Ketikkan no pilihan menu: ",end="")

#Input pilihan menu
menudipilih = int(input())

#MENENTUKAN AKSI SESUAI KONDISI MENU YANG DIPILIH
#KONDISI KETIKA MEMILIH MENU 1 (MEMBELI)
if menudipilih == 1:
    print(">> Transaksi pembelian")
    print("   Silahkan masukan no barang yang ingin anda beli: ",end="")
    idbarangdipilih = int(input())
    sibarang = daftar_barang[idbarangdipilih-1]
    transaksi = 0
    if stok[idbarangdipilih-1] > 0:
        print("   Masukkan jumlah kuantitas pembelian (maksimal: %d): "%(stok[idbarangdipilih-1]),end="")
        jumlah_pembelian = int(input())
        if(stok[idbarangdipilih-1] < jumlah_pembelian): 
            print("   %s hanya tersedia %d buah, Apakah Anda ingin memborong semuanya (1:iya atau 0:tidak)? "%(sibarang,stok[idbarangdipilih-1]),end="")
            borong_ngga = int(input())
            if borong_ngga == 1:
                transaksi = stok[idbarangdipilih-1] * harga_barang[idbarangdipilih-1]
                jumlah_pembelian =  stok[idbarangdipilih-1] #stok habis diborong :)
            else:
                print("   Transaksi Anda dibatalkan")
        else:
            transaksi = jumlah_pembelian * harga_barang[idbarangdipilih-1]
        
        #Proses pembayaran hanya dilakukan jika ada transaksi
        if transaksi != 0:
            #sebelumnya yang dicetak malah stock barang, harusnya jumlah pembelian
            print("   Nilai Transaksi Anda : ( %d x %d ) = %d"%(jumlah_pembelian , harga_barang[idbarangdipilih-1],transaksi))
            print("   -------------------------------------------------------------------------------------------------------")
            
            

            #--------------------- TAMBAHAN BARU DENGAN ADANYA DISCOUNT LOYALITAS BAGI MEMBER

            print("\n   Apakah anda memiliki akun membership (y/n):",end="")
            memb = input()
            potongan = 0 #default untuk nilai potongan
            if memb == 'y' or memb=='Y':
                un_pembeli = input("   > Masukkan user name membership Anda: ")
                id_memb = cari_member(daftarObjekMember,un_pembeli)
                if id_memb== -1:
                    print("   > Data akun member yang Anda masukkan salah, tidak ada poin yang dapat Anda gunakkan")
                else:
                    transaksi_awal = transaksi
                    print("   > Apakah Anda ingin menggunakan poin membership (y/n):",end="")
                    pake =  input()
                    if pake == 'y' or pake == 'Y':
                        print("   (i) Setiap poin bernilai 500 rupiah",end=" ")
                        print(", poin Anda :",daftarObjekMember[id_memb].poin,end=" ")
                        maksiPoin = daftarObjekMember[id_memb].poin
                        if maksiPoin > transaksi//500:
                            maksiPoin = transaksi//500
                        print(", poin maks dapat digunakkan pada transaksi:",maksiPoin)
                        poin_yg_digunakan = int(input("     Berapa poin yang ingin digunakkan: "))
                        while poin_yg_digunakan > maksiPoin:
                            print("       Nilai poin yang Anda masukkan terlalu besar")
                            poin_yg_digunakan = int(input("     + ulangi, berapa poin yang ingin digunakkan: "))
                        transaksi = transaksi - (poin_yg_digunakan*500)
                        potongan =  poin_yg_digunakan*500
                        print("       (i) Nilai Transaksi Anda, setelah potongan :",transaksi)
                        #poin berkurang karena digunakan untuk potongan nilai transaksi
                        daftarObjekMember[id_memb].poin = daftarObjekMember[id_memb].poin - poin_yg_digunakan
                        #update pertambahan nilai transaksi dari member
                        daftarObjekMember[id_memb].trx = daftarObjekMember[id_memb].trx + transaksi
                    
                    #poin bertambah dari transaksi terbaru jika transaksi sebelum potongan > 50000
                    if transaksi_awal >= 50000: 
                        daftarObjekMember[id_memb].poin = daftarObjekMember[id_memb].poin + 1
                        print("       (i) Anda member dan transaksi >= 50000 maka mendapatkan tambahan +1 poin dari transaksi ini")
                    

            #-------------------------------------------------------
            print("   -------------------------------------------------------------------------------------------------------")
            print("   Silahkan lakukan pembayaran!")
            # PENGGUNAAN ARRAY UNTUK MENDAFTARKAN NILAI MATA UANG YANG DAPAT DIGUNAKAN
            nilai_uang = [500,1000,2000,5000,10000,20000]

            # LOOPING PENGGUNA MEMASUKKAN UANG PEMBAYARAN 
            sisa_bayar = transaksi
            while sisa_bayar > 0:
                print("   Nilai uang yang Anda Masukan (1. 500 | 2. seribu | 3. 2ribu | 4. 5ribu | 5. 10ribu | 6.20 ribu ): ",end="")
                x_masuk = int(input())
                if x_masuk<=0 or x_masuk > len(nilai_uang):
                    print("   Nilai uang yang anda masukkan tidak valid")
                    continue
                print("   Anda memasukan uang sebesar",nilai_uang[x_masuk-1])
                sisa_bayar = sisa_bayar - nilai_uang[x_masuk-1]
                if sisa_bayar>0:
                    print("   Sudah membayar: %d dan sisa pembayaran: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                elif sisa_bayar==0:
                    print("   Sudah membayar: %d dan Lunas"%(transaksi-sisa_bayar))
                else:
                    print("   Sudah membayar: %d, Lunas dan nilai kembalian: %d, Pembayaran selesai"%(transaksi-sisa_bayar,(-1)*sisa_bayar))
            
            print("   -------------------------------------------------------------------------------------------------------")
            #BAGIAN KEMBALIAN, MENERAPKAN TEKNIK GREEDY AGAR JUMLAH UANG YANG DIKELUARKAN SEDIKIT
            if sisa_bayar<0:
                kembalian =  sisa_bayar*(-1)
                jmlh_lembar_peruang = [0]* len(nilai_uang) #mencatat berapa lembar untuk setiap jenis uang, sebagai kembalian
                i1 = len(nilai_uang)-1 #coba dari nilai uang terbesar
                while kembalian > 0:
                    if kembalian >= nilai_uang[i1]:
                        banyaklembar = kembalian//nilai_uang[i1] 
                        kembalian = kembalian - nilai_uang[i1] * banyaklembar
                        jmlh_lembar_peruang[i1] = banyaklembar
                    i1 = i1 - 1
                
                print("    Kembalian yang dikeluarkan mesin: ",end="")
                for i_jl in range(len(jmlh_lembar_peruang)):
                    if jmlh_lembar_peruang[i_jl] != 0:
                        print("(",jmlh_lembar_peruang[i_jl],"pecahan",nilai_uang[i_jl],")",end=" ")
                print()

            #menyiapkan info untuk update stock
            stok[idbarangdipilih-1]= stok[idbarangdipilih-1]-jumlah_pembelian #stok diupdate
            terjual[idbarangdipilih-1]= terjual[idbarangdipilih-1]+jumlah_pembelian #terjual diupdate
            if stok[idbarangdipilih-1] == 0: 
                print("    Stok barang terupdate, telah habis terjual")
            else:
                print("    Stok barang terupdate, telah terjual:",jumlah_pembelian)
            
            print("    Mesin mengeluarkan %d buah barang %s sesuai transaksi"%(jumlah_pembelian,sibarang))
            print("   -------------------------------------------------------------------------------------------------------")

            #MENULIS KE FILE DATA TRANSAKSI
            f = open("data_transaksi.txt", "a")
            waktu = str(datetime.now())
            f.write(waktu +","+ sibarang+","+str(jumlah_pembelian)+","+str(transaksi)+","+str(potongan)+"\n")
            f.close()

    #kondisi ketika barang kosong        
    else:
        print("   Maaf, saat ini %s tidak tersedia."%(sibarang))
    print("")

#OPSI KETIKA MEMILIH MENU 2 (MENAMPILKAN INFO NUTRISI)    
elif menudipilih == 2:
    print(">> Transaksi Mengecek Informasi Nutrisi")
    print("   Silahkan masukan no barang yang ingin anda lihat info nutrisinya: ",end="")
    id_barang = int(input())
    if id_barang >=1 and id_barang <= len(daftar_barang):
        print("   %s, harga : %d, dengan ketersediaan stok: %d"%(daftar_barang[id_barang-1],harga_barang[id_barang-1],stok[id_barang-1]))
        print("   Nutrisi: ",nutrisi[id_barang-1])

#KONDISI KETIKA MEMILIH MENU 3 (Fungsi Sekunder) 
elif menudipilih==3:
    print(">> Transaksi Manajemen Data")
    print("   Untuk melanjutkan silahkan masukkan username dan password (un pswd): ",end="")
    un,pswd = input().split(" ")
    #print(un,pswd)
    if un=="admin" and pswd=="123":
        print("   Login berhasil\n")
        print("   PILIHAN MENU ADMIN: ")
        print("\t-------------------------------------------------------------------------------------------------------")
        print("\t   1. data transaksi   |     2. add     |     3. edit      |     4. delete     |     5. Keluar")
        print("\t-------------------------------------------------------------------------------------------------------")
        print("\t   Menu Baru:")
        print("\t          6. Analisis data transaksi    |          7. cek expired date         |     8. cek member    ")
        print("\t-------------------------------------------------------------------------------------------------------")
        print("\n                                         Ketikkan no pilihan menu admin: ",end="")
        #Input pilihan menu
        menuadminterpilih = int(input())
        
        while menuadminterpilih != 5: #akan keluar ketika dipilih 5 pada menu admin
            if menuadminterpilih == 1:
                print("   >>> Melihat data transaksi")
                f = open("data_transaksi.txt", "r")
                nmr = 1
                totTRX = 0
                totPot = 0
                print("       ---------------------------------------------------------------------------------")
                print("        No.  Waktu                  Nama Barang       Jmlh   Transaksi nett    potongan")
                print("       ---------------------------------------------------------------------------------")
                for baris in f:
                    dataTRX = baris.split(",")
                    print("        %2d.  %s    %-15s    %3s   %14s        %5s"%(nmr,dataTRX[0][:19],dataTRX[1],dataTRX[2],dataTRX[3],dataTRX[4]),end="")
                    totTRX = totTRX + int(dataTRX[3])
                    totPot = totPot + int(dataTRX[4])
                    nmr = nmr+1 
                f.close()
                print("       ---------------------------------------------------------------------------------")
                print("        (i) transaksi nett adalah nilai transaksi setelah potongan")
                print("        + Total nilai transaksi Nett: ",totTRX)
                print("        + Total nilai potongan      : ",totPot)
                print("       ---------------------------------------------------------------------------------")
                
            
            elif menuadminterpilih == 2:
                print("   >>> Add data barang baru")
                nm_brng  = input("   Masukkaan data nama barang: ")
                hrg_brng = int(input("   Masukkaan data harga: "))
                stok_brng = int(input("   Masukkaan data stok: "))
                tgl_exp = input("   Masukkaan data expired date yyyy-mm-dd: ")
                nutri  = input("   Masukkaan data nutrisi barang (akhiri dengan .): ")
                #masukkan ke array
                daftar_barang.append(nm_brng)
                harga_barang.append(hrg_brng)
                stok.append(stok_brng)
                terjual.append(0)
                expired_date.append(tgl_exp)
                nutrisi.append(nutri)
                print("   Data",nm_brng,"telah tersimpan")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")

                
            elif menuadminterpilih == 3:
                print("   >>> Edit data barang")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")
                idtarget = int(input("   Masukkaan nomor barang yang ingin diedit: "))
                print("   Data %s akan diedit."%(daftar_barang[idtarget-1]))
                daftar_barang[idtarget-1]  = input("   Masukkaan data baru nama barang: ")
                harga_barang[idtarget-1] = int(input("   Masukkaan data baru harga: "))
                stok[idtarget-1]  = int(input("   Masukkaan data baru stok: "))
                expired_date[idtarget-1]  = input("   Masukkaan data baru tanggal expired (yyyy-mm-dd): ")
                print("   Proses edit data selesai")

            elif menuadminterpilih == 4:
                print("   >>> Delete data barang")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")
                idtarget = int(input("   Masukkaan nomor barang yang ingin didelete: "))
                print("   Anda yakin data %s akan didelete ? (y/n): "%(daftar_barang[idtarget-1]),end="")
                keputusan = input()
                if keputusan=='y' or keputusan=='Y':
                    barangyangdidelete = daftar_barang[idtarget-1]
                    daftar_barang.pop(idtarget-1)
                    harga_barang.pop(idtarget-1)
                    stok.pop(idtarget-1)
                    terjual.pop(idtarget-1)
                    expired_date.pop(idtarget-1)
                    nutrisi.pop(idtarget-1)
                    print("   Data %s telah didelete"%(barangyangdidelete))
                else:
                    print("   Proses delete data %s dibatalkan"%(daftar_barang[idtarget-1]))

            elif menuadminterpilih == 6:
                print("   >>> Analisis data transaksi")
                N = len(daftar_barang)
                #mempaketkan data pada array ke dalam objek (dari kelas barang)
                #pada bagian atas sudah mengimport pustaka_tambahan.py
                #pustaka_tambahan.py tempat mendefinisikan KelasBarang
                DaftarObjekBarang=[]
                for i in range(N):
                    objBarang = KelasBarang(daftar_barang[i],harga_barang[i],stok[i],terjual[i],expired_date[i],nutrisi[i])
                    DaftarObjekBarang.append(objBarang)

                #urutkan tingkat laku tidaknya barang berdasarkan nilai kuantitas terjual
                DaftarObjekBarangTerurut = sorted(DaftarObjekBarang, key=lambda m: m.terjual, reverse=True)
                #memanggil fungsi cetak_daftar_objek_barang() untuk mencetak array DaftarObjekBarangTerurut
                cetak_daftar_objek_barang(DaftarObjekBarangTerurut)

            elif menuadminterpilih == 7:
                print("   >>> Cek Expired Date Barang (terurut dari waktu expired terdekat)")
                N = len(daftar_barang)
                #memaketkan data pada array ke dalam objek (dari kelas barang)
                #pada bagian atas sudah mengimport pustaka_tambahan.py
                #pustaka_tambahan.py tempat mendefinisikan KelasBarang
                DaftarObjekBarang=[]
                for i in range(N):
                    objBarang = KelasBarang(daftar_barang[i],harga_barang[i],stok[i],terjual[i],expired_date[i],nutrisi[i])
                    DaftarObjekBarang.append(objBarang)

                #urutkan tingkat laku tidaknya barang berdasarkan nilai kuantitas terjual
                DaftarObjekBarangTerurutExpDate = sorted(DaftarObjekBarang, key=lambda m: m.expired_date)
                #memanggil fungsi cetak_daftar_objek_barang() untuk mencetak array DaftarObjekBarangTerurut
                cetak_daftar_exp_date_barang(DaftarObjekBarangTerurutExpDate)

            elif menuadminterpilih == 8:
                print("   >>> Cek Data Member (terurut dari member dengan transaksi terbesar)")
                #urutkan member berdasarkan nilai transaksi yang dilakukannya
                daftarObjekMemberTerurut = sorted(daftarObjekMember, key=lambda m: m.trx,reverse=True)
                cetak_daftar_member(daftarObjekMemberTerurut)


            else :
                print("   Pilihan data menu tidak valid. Silahkan masukan kembali")
            print("\n                                         Ketikkan no pilihan menu admin: ",end="")
            #Input lagi pilihan menu
            #----------------------------------------
            f = open("data_aplikasi.csv", "w")
            f.write("")
            f.close()

            #baru append
            f = open("data_aplikasi.csv", "a")
            for i in range(len(daftar_barang)):
                f.write(daftar_barang[i]+","+str(harga_barang[i])+","+str(stok[i])+","+str(terjual[i])+","+str(expired_date[i])+","+ nutrisi[i].strip()+"\n")
            f.close()
            #---------------------------------------
            menuadminterpilih = int(input())
    
            

    else:
        print("   Login gagal, keluar aplikasi")

#KONDISI KETIKA MEMILIH MENU 4 (Fungsi Keluar) 
elif menudipilih == 4:
    print("Anda memilih keluar aplikasi")

#KONDISI KETIKA MEMILIH MENU 5 (Daftar Membership) 
elif menudipilih == 5:
    print(">> Daftar Membership")
    print("   Keuntungan: Anda akan mendapatkan 1 poin setiap melakukan transaksi >= 50000 (lima puluh ribu)")
    print("               Setiap poin dapat ditukarkan sebagai cahback belanja sebesar 500")
    user_name = input("   Mulai mendaftar!!! Masukkan user name (tanpa_spasi & huruf kecil): ")
    id = cari_member(daftarObjekMember,user_name)
    # dipastikan user name dari member tidak boleh yang sudah ada
    while id != -1:
        print("   (!) user name sudah terdaftar, gunakan user name yang lain")
        user_name = input("   Masukkan user name (tanpa_spasi & huruf kecil): ")
        id = cari_member(daftarObjekMember,user_name)
    no_telp =  input("   Masukkan no telepon: ")
    new_member = KelasMember(user_name,no_telp,0,0)
    f = open("data_member.csv", "a")
    f.write(user_name+","+no_telp+","+str(0)+str(0)+"\n")
    f.close()
    #tambahkan ke array daftarObjekMember
    daftarObjekMember.append(new_member)
    print("   Member dengan nama",user_name,"berhasil mendaftar.")

#KONDISI KETIKA MEMILIH MENU SELAINNYA 
else:
    print("Masukkan anda untuk pilihan menu tidak sesuai")

print("Transaksi Selesai! silahkan run kembali aplikasi ini untuk transaksi selanjutnya :)\n")

#OPERASI FILE UNTUK MENDUKUNG UPDATE DATA STOCK
#menulis ke file dengan nilai data barang yang terakhir
#apus dulu
f = open("data_aplikasi.csv", "w")
f.write("")
f.close()

#baru append
f = open("data_aplikasi.csv", "a")
for i in range(len(daftar_barang)):
    f.write(daftar_barang[i]+","+str(harga_barang[i])+","+str(stok[i])+","+str(terjual[i])+","+str(expired_date[i])+","+ nutrisi[i].strip()+"\n")
 
#OPERASI FILE UNTUK MENDUKUNG UPDATE POIN MEMBER ---------------------------------------------------NEW VERSION
#menulis ke file dengan nilai poin member yang terakhir
#apus dulu
f = open("data_member.csv", "w")
f.write("")
f.close()

#baru append
f = open("data_member.csv", "a")
for i in range(len(daftarObjekMember)):
    f.write(daftarObjekMember[i].nama+","+daftarObjekMember[i].notelepon+","+str(daftarObjekMember[i].poin)+","+str(daftarObjekMember[i].trx)+"\n")
f.close()