from datetime import date
    

class KelasBarang:
    def __init__(self, n, h,s,t,e,n2):
        self.nama = n
        self.harga = h
        self.stok = s
        self.terjual = t
        self.expired_date = e
        self.nutrisi = n2

def cetak_daftar_objek_barang(barang_list):
    i = 0
    print("       -------------------------------------------------------------------------------------------------------------------------")
    print("       Rank  Terjual       Nama          Harga    Stok                    Rekomendasi (!)")
    print("       -------------------------------------------------------------------------------------------------------------------------")    
    for barang in barang_list:
        i = i + 1
        print("       %2d    %7d   %-15s %7d      %2d   %s"%(i,barang.terjual, barang.nama, barang.harga,barang.stok,fungsi_rekomendasi(barang.terjual,barang.harga)),)
    print("       -------------------------------------------------------------------------------------------------------------------------")

def fungsi_rekomendasi(jumlah_terjual,harga):
    if jumlah_terjual >= 100:
        return "Naikkan harga (+1000) menjadi "+str(harga + 1000)
    elif jumlah_terjual >= 50:
        return "Naikkan harga (+500) menjadi "+str(harga + 500)
    elif jumlah_terjual <= 10 and jumlah_terjual > 0:
        return "Beri harga promosi (-1000) menjadi "+str(harga - 1000)
    elif jumlah_terjual==0:
        rekomHarga = round(harga/2) - (round(harga/2)%500)  
        return "Belum terjual satupun, beri promosi (sekitar 1/2 harga) menjadi "+str(round(rekomHarga))
    else:
        return "Pertahankan harga"
    

class KelasMember:
    def __init__(self, na, nt, p, t):
        self.nama = na
        self.notelepon = nt
        self.poin = p
        self.trx = t #nilai transaksi real (nett, sudah potongan)

def cari_member(M, un_dicari):
    N = len(M)
    for i in range(N):
        member = M[i]
        if member.nama == un_dicari:
            return i
    return -1  # Jika tidak ditemukan



from datetime import datetime
from dateutil.relativedelta import relativedelta

def hitung_selisih_tanggal(tanggal_awal, tanggal_akhir):
    # Mengubah string tanggal menjadi objek datetime
    tanggal_awal = datetime.strptime(tanggal_awal, "%Y-%m-%d")
    tanggal_akhir = datetime.strptime(tanggal_akhir, "%Y-%m-%d")
    # Menghitung selisih hari
    selisih_hari = (tanggal_akhir - tanggal_awal).days
    return formatingTahunBulanMingguHari(selisih_hari)

def formatingTahunBulanMingguHari(hari):
    tahun = hari//365
    bulan  = (hari%365) // 30
    minggu = ((hari % 365)%30)//7
    hari = ((hari % 365)%30)%7
    strnya = ""
    if tahun >0:
        strnya = strnya + str(tahun)+" tahun "
    if bulan>0:
        strnya = strnya + str(bulan)+" bulan "
    if minggu>0:
        strnya = strnya + str(minggu)+" minggu "
    if hari>0:
        strnya = strnya + str(hari)+" hari"
    return strnya

def cetak_daftar_exp_date_barang(DaftarBarang):
    i = 0
    print("       -------------------------------------------------------------------------------------------------------------------------")
    print("       No.  Expired Date       Nama          Harga    Stok                    Catatan (!)")
    print("       -------------------------------------------------------------------------------------------------------------------------")    
    today = str(date.today())
    for barang in DaftarBarang:
        if barang.stok != 0:
            i = i + 1
            print("       %2d    %10s   %-15s %7d      %2d     %s"%(i,barang.expired_date, barang.nama, barang.harga,barang.stok, hitung_selisih_tanggal(today, barang.expired_date)))
    print("       -------------------------------------------------------------------------------------------------------------------------")


def cetak_daftar_member(DaftarMember):
    i = 0
    print("       ---------------------------------------------------------------------------------------------------------------------------")
    print("        No.  User Name       No Telepon     Poin      Transaksi             Catatan (!)")
    print("       ---------------------------------------------------------------------------------------------------------------------------")    
    today = str(date.today())
    for x in DaftarMember:
        i = i + 1
        print("       %2d    %-10s     %-15s %4d    %10d     %s"%(i, x.nama , x.notelepon, x.poin, x.trx, komentar(x)))
    print("       ---------------------------------------------------------------------------------------------------------------------------")


def komentar(member):
    if member.trx >= 100000:
        return "Langganan: transaksi sudah lebih dari seratus ribu rupiah"
    elif member.trx >= 50000:
        return "Potensial: transaksi sudah lebih dari limapuluh ribu rupiah"
    elif member.trx==0:
        return "Member baru"
    return "Pembeli biasa: transaksi masih di bawah limapuluh ribu rupiah."