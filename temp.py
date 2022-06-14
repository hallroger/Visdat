import copy

def isibrg():
    barang = [[100, "Bayam"   , "sayuran" , 15, 1500 , 0, 0, 0],
              [200, "Kangkung", "sayuran" , 10, 1000 , 0, 0, 0],
              [300, "Beras"   , "pokok"   , 25, 10000, 0, 0, 0],
              [400, "Kerupuk" , "tambahan", 20, 1250 , 0, 0, 0],
              [500, "Ubi"     , "pokok"   , 15, 2000 , 0, 0, 0],
              [600, "Wortel"  , "sayuran" , 20, 4000 , 0, 0, 0]]
    return barang
              
def isijual():
    jual = [["10-10-20",200,1,1200 ,5 ],
            ["10-10-20",300,2,12000,10],
            ["10-10-20",200,1,900  ,0 ],
            ["10-10-20",100,1,2500 ,0 ],
            ["10-10-20",600,2,5000 ,5 ],
            ["12-10-20",400,2,1500 ,0 ],
            ["12-10-20",200,3,1500 ,0 ],
            ["13-10-20",100,1,2500 ,25],
            ["13-10-20",200,3,1500 ,10],
            ["13-10-20",300,1,15000,10]]
    return jual

def buatarray(barang,jual):
    print("Data pembelian : ")
    for i in range(len(barang)):
        print("Kode Barang : ",barang[i][0])
        print("nama Barang : ",barang[i][1])
        print("jenis Barang : ",barang[i][2])
        print("jumlah Barang : ",barang[i][3])
        print("harga beli Barang : ",barang[i][4])
        print("sisa Barang : ",barang[i][5])
        print("untung Barang : ",barang[i][6])
        print("Ketersediaan barang : ",barang[i][7])
        print("==================================")
    print("\n")
    print("Data penjualan : ")
    for j in range(len(jual)):
        print("tanggal : ",jual[j][0])
        print("kode : ",jual[j][1])
        print("jumlah : ",jual[j][2])
        print("harga : ",jual[j][3])
        print("diskon : ",jual[j][4])
        print("==================================")

def bubbleSort(barang):
    n = len(barang)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if barang[j][2] > barang[j + 1][2] :
                barang[j], barang[j + 1] = barang[j + 1], barang[j]

def sisabarang(brg,jual,sdh):
    if (sdh == True):
        barang = copy.deepcopy(brg)
    else : 
        barang = brg
    
    for i in range(len(barang)):
        if (barang[i][5]==0):
            barang[i][5]=barang[i][3]

    for j in range(len(barang)):
        print("Kelompok barang :", barang[j][0], barang[j][1])
        print('{:^12} {:^10} {:^8} {:^10}'.format("Tanggal","Harga Asli","Sisa","jml_Untung")) 
        for i in range(len(jual)):
            if barang[j][0] == jual[i][1]:
                barang[j][6] = barang[j][6]+(((jual[i][3]*((100-jual[i][4])/100))-barang[j][4])*jual[i][2])
                barang[j][5] = barang[j][5]-jual[i][2]
                print('{:^10} {:^14} {:^1} {:^18}'.format(jual[i][0],jual[i][3],barang[j][5],barang[j][6])) 
        print("\n")

def laporan(barang):
    pokok = sayuran = tambahan = 0
    for i in range(len(barang)):
        if barang[i][2] == "sayuran":
            sayuran += barang[i][6]
        elif barang[i][2] == "pokok":
            pokok += barang[i][6]
        elif barang[i][2] == "tambahan" :
            tambahan += barang[i][6]

    print("1 pokok",pokok)
    print("2 sayuran",sayuran)
    print("3 tambahan",tambahan)
    print("Total untung adalah :",pokok+sayuran+tambahan)

def tambahbar(barang):
    kodebar = int(input("Masukan kode barang : "))
    kodebar1 = search(kodebar,barang)
    if (kodebar1!=None) : 
        print("Kode barang sudah ada")
    else : 
        namabar = str(input("Masukan nama barang : "))
        jenisbar = str(input("Masukan jenis barang : "))
        jumlahbar = int(input("Masukan jumlah barang : "))
        hargabar = int(input("Masukan harga barang : "))
        barang.append([kodebar,namabar,jenisbar,jumlahbar,hargabar,0,0,0])

def search(kode,barang):
    for i in range(len(barang)):
        if (kode==barang[i][0]):
            return i
    else :
        return None

def ubah(barang):
    kodebar = search(int(input("Masukan kode barang : ")),barang)
    if (kodebar==None) : 
        print("Kode barang tidak ditemukan")
    else : 
        pil = False 
        while (pil == False) :
            print("1. Nama dan Jenis barang")
            print("2. Nama dan Jumlah barang")
            print("3. Jenis dan Jumlah barang")
            pilihan = int(input("pilih bagian mana yang akan dirubah : "))
            if (pilihan == 1):
                barang[kodebar][1] = str(input("Masukan nama barang : "))
                barang[kodebar][2] = str(input("Masukan jenis barang : "))
                pil = True
            elif (pilihan == 2):
                barang[kodebar][1] = str(input("Masukan nama barang : "))
                barang[kodebar][3] = int(input("Masukan jumlah barang : "))
                pil = True
            elif (pilihan == 3):
                barang[kodebar][2] = str(input("Masukan jenis barang : "))
                barang[kodebar][3] = int(input("Masukan jumlah barang : "))
                pil = True

def tersedia(barang):
    for i in range(len(barang)):
        pil = False 
        while (pil == False) : 
            print("Kode Barang : ",barang[i][0])
            sedia = str(input("Ketersediaan barang (Y/N):  "))
            if (sedia=="Y" or sedia=="y"):
                barang[i][7] = 1
                pil = True
            elif (sedia=="N" or sedia=="n"):
                barang[i][7] = 0
                pil = True

sudah = False
status = False

while (status == False) :
    print("Menu Utama")
    print("1. Isi File Barang")
    print("2. Show Isi File")
    print("3. Tambah barang")
    print("4. Ubah barang")
    print("5. Revisi keaktifan")
    print("6. Sisa barang")
    print("7. Laporan")
    print("8. Exit")
    pil = int(input("Masukan pilihan : "))
    if (pil==1):
        print("data sudah diisi")
        barang = isibrg()
        jual = isijual()
    elif (pil==2):
        buatarray(barang,jual)
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==3):
        tambahbar(barang)
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==4):
        ubah(barang)
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==5):
        tersedia(barang)
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==6):
        print("Laporan sisa barang")
        sisabarang(barang,jual,sudah)
        sudah = True 
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==7):
        print("Laporan keuntungan setiap barang")
        laporan(barang)
        input("Jika sudah selesai melihat dapat menekan enter")
    elif(pil==8):
        status = True