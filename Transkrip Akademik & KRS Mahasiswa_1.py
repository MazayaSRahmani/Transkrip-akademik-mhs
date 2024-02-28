from tabulate import tabulate

head_transkrip = ["Index","Mata Kuliah","Nilai","Mutu Huruf","Sks"]
transkrip = [
    [101, "Pengantar Komunikasi", 4, 'A', 4],
    [201, "Jurnalisme Data", 3.5,'B',6],
    [301, "Reportase Investigasi", 4,'A', 6],
    [303, "Penulisan Berita Mendalam", 3.75,'A', 3],
    [401, "Jurnalisme Advokasi", 2.5,'C', 3],
    [501, "Sistem, Hukum & Etika Pers", 4,'A', 2]
]

head_krs_aktif = ["Index","Mata Kuliah","Sks"]
krs_aktif = [
    [601, "Seminar Proposal", 4],
    [602, "Manajemen & Produksi Media Massa", 3]
]

head_krs_pilihan = ["Index","Mata Kuliah","Sks"]
krs_pilihan = [
    [701, "Skripsi",4],
    [702, "Praktik Kerja Jurnalistik",6]
]

def line():
    print('========================================================================\n')
    
def end_administrator():
    print('''
Program telah diakhiri.
Terima kasih!        
          ''')

def end_mahasiswa():
    print('''
Program telah diakhiri.
Terima kasih, semangat berkuliah selalu!
          ''') 

def pilihan_akun():
    print("""
---------------------------------
            Pilihan Akun
---------------------------------
Masuk sebagai:
1. Administrator
2. Mahasiswa
---------------------------------

Masukkan pilihan akun sesuai nomor pada menu.
        """)

def main_menu():
    print("""
---------------------------------
        TRANSKRIP AKADEMIK
---------------------------------
Daftar Menu:
1. Tampilkan Transkrip Akademik
2. Tambah Data Transkrip Akademik
3. Edit Transkrip Akademik
4. Hapus Data Transkrip Akademik
5. Exit Program
6. Ganti Akun
---------------------------------
        """)
    
def read_menu_func():
    print("""
---------------------------------------
                READ MENU
---------------------------------------
List Menu:
1. Tampilkan seluruh transkrip akademik
2. Cari data transkrip akademik
3. Tampilkan permintaan persetujuan KRS 
4. Kembali ke Menu Utama
5. Keluar program
---------------------------------------
        """)
    
def create_menu_func():
    print("""
---------------------------------
            CREATE MENU
---------------------------------
List Menu:
1. Tambah Data Transkrip 
2. Kembali ke Menu Utama
3. Keluar program
---------------------------------
          """)

def update_menu_func():
    print("""
---------------------------------
            UPDATE MENU
---------------------------------
List Menu:
1. Edit Transkrip 
2. Kembali ke Menu Utama
3. Keluar program
---------------------------------
          """)
    
def delete_menu_func():
    print("""
---------------------------------
            DELETE MENU
---------------------------------
List Menu:
1. Hapus Baris Data Transkrip
2. Hapus Seluruh Data Transkrip
3. Kembali ke Menu Utama
4. Keluar program
---------------------------------
          """)

def main_menu_mahasiswa():
    print("""
---------------------------------
            MENU UTAMA
---------------------------------
Daftar Menu:
1. Transkrip Akademik
2. Kartu Rencana Studi
3. Kartu kemajuan Studi
4. Exit Program
5. Ganti Akun
---------------------------------
        """)
    
def read_menu_mahasiswa():
    print("""
---------------------------------------
            TRANSKRIP AKADEMIK
---------------------------------------
List Menu:
1. Tampilkan seluruh transkrip akademik
2. Cari data transkrip akademik
3. Kembali ke Menu Utama
4. Keluar program
---------------------------------------
        """)
    
def krs_menu__mahasiswa():
    print("""
---------------------------------
            KRS MENU
---------------------------------
List Menu:
1. Tampilkan seluruh KRS aktif
2. Tampilkan seluruh KRS pilihan
3. Kembali ke Menu Utama
4. Keluar program
---------------------------------
          """)

def kks_menu_mahasiswa():
    print("""
---------------------------------
            KKS MENU
---------------------------------
List Menu:
1. Tampilkan Kartu Kemajuan Studi
2. Kembali ke Menu Utama
3. Keluar program
---------------------------------
          """)
    
def transkrip_table():
    print('\n')
    print("""
                TRANSKRIP AKADEMIK MAHASISWA JURNALISTIK
                        FAKULTAS ILMU KOMUNIKASI""")
    print("""
Nama : Justito Adiprasetyo
NPM  : 210610200066""")
    print(tabulate(transkrip, headers=head_transkrip, tablefmt="fancy_grid"))
    
def kalkulator_mutu_huruf(nilai):
    if 3.50 <= nilai_int <= 4.00:
        return 'A'
    elif 2.50 <= nilai_int < 3.50:
        return 'B'
    elif 1.50 <= nilai_int < 2.50:
        return 'C'
    elif nilai_int < 1.50:
        return 'D'
        
def show_1_row(matkul):
    try:
        if transkrip != []:
            for i in transkrip:
                if i[1] != matkul:
                    continue
                elif i[1] == matkul:
                    tabel_cari_matkul = [i]
                    print(tabulate(tabel_cari_matkul, headers=head_transkrip, tablefmt='fancy_grid'))
                    break
            if i[1] != matkul:
                print(f"Mata kuliah {matkul} tidak ditemukan, mohon masukkan nama mata kuliah dengan benar.")
        else:
            print("Tabel Transkrip Akademik Kosong.")
    except:
        print("input invalid")

def sort_table_transkrip(nama_kolom,desc):
    try:
        index_head = head_transkrip.index(nama_kolom)
        sorted_table = tabulate(sorted(transkrip, key = lambda x:x[index_head],reverse=desc),head_transkrip, tablefmt='fancy_grid')
        print(sorted_table)
    except:
        print("input invalid")

def invalid_input():
    print("Masukkan pilihan menu yang benar!")
    
def krs_table():
    print('\n')
    print("""
                    KARTU RENCANA STUDI
                    MAHASISWA JURNALISTIK
                  FAKULTAS ILMU KOMUNIKASI""")
    print("""
Nama : Justito Adiprasetyo
NPM  : 210610200066""")
    print(tabulate(krs_aktif, headers=head_krs_aktif, tablefmt="fancy_grid"))

def krs_pilihan_table():
    print('\n')
    print("""
                    KARTU RENCANA STUDI
                    MAHASISWA JURNALISTIK
                  FAKULTAS ILMU KOMUNIKASI""")
    print("""
Nama : Justito Adiprasetyo
NPM  : 210610200066""")
    print(tabulate(krs_pilihan, headers=head_krs_pilihan, tablefmt="fancy_grid"))

def kks_table():
    print('\n')
    print("""
                                KARTU KEMAJUAN STUDI 
                                MAHASISWA JURNALISTIK
                              FAKULTAS ILMU KOMUNIKASI""")
    print("""
Nama : Justito Adiprasetyo
NPM  : 210610200066""")
    print(tabulate(transkrip, headers=head_transkrip, tablefmt="fancy_grid"))
    
def sub_menu_krs():
    print('''
    ---------------------------------
                EDIT KRS
    ---------------------------------
    List Menu:
    1. Menambahkan kelas 
    2. Mengurangi kelas
    3. Kembali ke Menu Utama
    4. Keluar program
    ---------------------------------   

          ''')

while True:
    pilihan_akun()
    akun = input(f"Pilih akun: ")
    
    if akun == '1':
        print("Berhasil masuk dengan akun administrator!")
        while True:
            main_menu()
            menu = input(f"Masukkan angka Menu yang ingin dijalankan: ")
            
            if menu == '1':
                
                while True:
                    line()
                    read_menu_func()
                    read_menu = input("Masukkan angka Menu yang ingin dijalankan: ")
                    
                    if read_menu == '1':
                        transkrip_table()
                        print('\n\nApakah anda ingin mengurutkan tampilan transkrip akademik?')
                        tanya_sort_transkrip = input("Ya / Tidak : ").title()
                        
                        if tanya_sort_transkrip == 'Ya':
                            kolom_transkrip = input("Urutkan transkrip akademik berdasarkan kolom: ").title()
                            sort_by_transkrip = int(input("Urutkan dari nilai minimum (0) atau nilai maksimum (1): "))
                            sort_table_transkrip(kolom_transkrip,sort_by_transkrip)
                        elif tanya_sort_transkrip == 'Tidak':
                            break
                        else:
                          print("Mohon masukkan pilihan menu yang benar!")  
                        
                    elif read_menu == '2':
                        cari_matkul = input("Masukkan nama mata kuliah yang dicari dari transkrip akademik: ").title()
                        show_1_row(cari_matkul)
                        
                    elif read_menu == '3':
                        permintaan_krs = []
                        print(tabulate(permintaan_krs, headers=head_krs_aktif, tablefmt='fancy_grid'))
                    
                    elif read_menu == '4':
                        break
                    
                    elif read_menu == '5':
                        end_administrator()
                        exit()
                    
                    else:
                        print("Mohon masukkan pilihan menu yang benar!")
            
            elif menu == '2':
                while True:
                    line()
                    create_menu_func()
                    create_menu = input("Masukkan angka Menu yang ingin dijalankan: ")
                    
                    if create_menu =='1':
                        mata_kuliah = input("\nMasukan nama mata kuliah: ").title()
                        while True:
                            if not mata_kuliah.isdigit():
                                for i in transkrip:
                                    if i[1] != mata_kuliah:
                                        continue
                                    elif i[1] == mata_kuliah:
                                        print(f"Mata kuliah {mata_kuliah} telah terdata pada transkrip akademik!")
                                        mata_kuliah = input("\nMasukan nama mata kuliah: ").title()
                                break 
                            else:
                                print("Nama mata kuliah tidak boleh hanya berbentuk angka!")
                                mata_kuliah = input("\nMasukan nama mata kuliah: ").title()             
                            
                        nilai = input("Masukkan nilai mata kuliah: ")
                        nilai_int = 0
                        while True:
                            if nilai.replace('.', '', 1).isdigit() and float(nilai) <= 4:
                                nilai_int = float(nilai)
                                break
                            elif  nilai.isalnum() or nilai.isalpha(): 
                                print("Mohon masukkan besaran nilai sesuai format angka (0.0 - 4.0)!")
                                nilai = input("Masukkan nilai mata kuliah: ")

                        SKS = input("Masukkan jumlah SKS: ")
                        SKS_int = 0
                        while True:
                            if SKS.isdigit() and int(SKS) <= 6:
                                SKS_int = int(SKS)
                                break
                            elif  SKS.isalnum() or SKS.isalpha(): 
                                print("Mohon masukkan besaran SKS sesuai format angka (1 - 6)!")
                                SKS = input("Masukkan jumlah SKS: ")
                        
                        index = transkrip[-1][0] + 1  
                        mutu_huruf = kalkulator_mutu_huruf(nilai)
                        
                        records = [[index, mata_kuliah, nilai, mutu_huruf, SKS]]
                        print(tabulate(records, headers=head_transkrip, tablefmt="fancy_grid"))
                        
                        print("\nApakah anda yakin ingin menyimpan data berikut? ")
                        konfirmasi = input("Ya / Tidak : ").title()
                        if konfirmasi =='Ya':
                            records = [index, mata_kuliah, nilai, mutu_huruf, SKS]
                            transkrip.append(records)
                            print("\nInput data berhasil!\n")
                            transkrip_table()
                        elif konfirmasi =='Tidak':
                            print("\nInput data dibatalkan!")
                            continue
                    elif create_menu == '2':
                        break
                    elif create_menu == '3':
                        end_administrator()
                        exit()
                    else:
                        print("Mohon masukkan pilihan menu yang benar!")
            
            elif menu == '3':
                while True:
                    line()
                    update_menu_func()
                    update_menu = input('Masukkan angka menu yang ingin dijalankan: ')
                    if update_menu == '1':
                        transkrip_table()
                        mata_kuliah_update = input("\nMasukan nama mata kuliah untuk diupdate: ").title()
                        for i in range(len(transkrip)):
                            for i in transkrip:
                                if i[1] != mata_kuliah_update:
                                    continue
                                
                                elif i[1] == mata_kuliah_update:
                                    show_1_row(mata_kuliah_update)
                                    pilih_update = input("Pilih kolom untuk di update: ").title()
                                    
                                    if pilih_update == 'Index':
                                        print("Index tidak bisa diinput oleh user!")
                                        break
                                    elif pilih_update == 'Mata Kuliah':
                                        while True:
                                            update_data_matkul = input("Ubah matkul menjadi: ").title()
                                            for i in transkrip:
                                                if i[1] != update_data_matkul:
                                                    continue
                                                elif i[1] == update_data_matkul:
                                                    print(f'Mata kuliah {update_data_matkul} telah terdata!')
                                            break
                                            
                                        konfirmasi_update = input("Apakah anda yakin untuk melanjutkan edit (Ya/ Tidak): ").title()
                                        if konfirmasi_update == 'Ya':
                                            for i in transkrip:
                                                if i[1] == mata_kuliah_update:
                                                    i[1] = update_data_matkul.title()
                                                    transkrip_table()
                                                    break
                                                menu = '3'
                                        elif konfirmasi_update != 'Ya':
                                            print("Perubahan dibatalkan!")
                                            break
                                        
                                    elif pilih_update == 'Nilai':
                                        nilai_int = 0 
                                        while True:
                                            update_data_nilai = input("Ubah nilai menjadi: ")
                                            if update_data_nilai.replace('.', '', 1).isdigit():
                                                nilai_int = float(update_data_nilai)
                                                
                                                if nilai_int<= 4.0 and nilai_int>= 0.0 :
                                                    for i in transkrip:
                                                        if i[1] == mata_kuliah_update:
                                                            i[2] = update_data_nilai
                                                            i[3] = kalkulator_mutu_huruf(nilai_int)
                                                            transkrip_table()
                                                            break
                                                    break
                                                else: 
                                                    print("Mohon masukkan besaran nilai sesuai format angka (0.0 - 4.0)!")
                                            else:
                                                print("Mohon masukkan besaran nilai sesuai format angka (0.0 - 4.0)!")
                                                                                        
                                    elif pilih_update == 'Mutu Huruf':
                                        print("Mutu huruf tidak bisa diinput oleh user!")
                                        break
                                    elif pilih_update == 'Sks':
                                        
                                        while True:
                                            update_data_sks = input("Ubah sks menjadi: ")
                                            if update_data_sks.isnumeric() and float(update_data_sks) <= 6:
                                                False
                                            elif  update_data_sks.isalnum() or update_data_sks.isalpha(): 
                                                print("Mohon masukkan besaran SKS sesuai format angka (0.0 - 4.0)!")
                                                update_data_sks = input("Masukkan SKS mata kuliah: ")                              
                                            for i in transkrip:
                                                if i[1] == mata_kuliah_update:
                                                    i[4] = update_data_sks
                                                    transkrip_table()
                                                    break
                                            break
                                    else:
                                        print("Masukkan menu yang benar!(Mata Kuliah / Nilai / SKS)")      
                            break    
                        
                            
                    elif update_menu == '2':
                        break
                    
                    elif update_menu == '3':
                        end_administrator()
                        exit()
                        
                    else:
                        print("Mohon masukkan pilihan menu yang benar!")
                
            elif menu == '4':
                while True:
                    line()
                    delete_menu_func()
                    delete_menu = input("Masukkan angka Menu yang ingin dijalankan: ")
            
                    if delete_menu == '1':
                        transkrip_table()
                        input_user= int(input('masukkan index: '))
                        input_index = 0
                        for i, baris in enumerate(transkrip):
                            if baris[0] == input_user:
                                print("Index ditemukan!")
                                input_index = i
                                print(input_index)
                                break
                                
                        if input_index != None:
                            for i, baris in enumerate(transkrip):
                                if i == input_index:
                                    print(baris[0])
                                    show_1_row(input_index)
                            del transkrip[input_index]
                            print("\nData berhasil dihapus!\n")
                            transkrip_table()
                        else:
                            print("Index tidak ditemukan!")
                        
                    elif delete_menu == '2':
                        print('\n\nApakah anda yakin untuk menghapus semua data transkrip akademik?')
                        print('\nData yang telah terhapus TIDAK BISA DIKEMBALIKAN.\n')
                        konfirmasi_clear = input("Ya / Tidak : ").title()
                        if konfirmasi_clear == 'Ya':
                            transkrip.clear()
                            print('Seluruh data berhasil dihapus!')
                            transkrip_table()
                        elif konfirmasi_clear == 'Tidak':
                            True
                        else:
                            print('\nMasukkan pilihan menu yang benar!')
                            
                    elif delete_menu == '3':
                        break
                    elif delete_menu == '4':
                        end_administrator()
                        exit()
                    else:
                        print('Masukkan pilihan menu yang benar!')
                           
            elif menu == '5':
                end_administrator()
                exit()
            
            elif menu == '6':
                break
            
            else:
                print('Masukkan pilihan menu yang benar!')
            
            
    elif akun == '2':
        print("Berhasil masuk dengan akun mahasiswa!")
        while True:
            main_menu_mahasiswa()
            menu = input(f"Masukkan angka Menu yang ingin dijalankan: ")
            
            if menu == '1':
                while True:
                    read_menu_mahasiswa()
                    read_menu = input("Masukkan angka menu yang ingin dijalankan: ")
                    if read_menu == '1':
                        transkrip_table()
                    elif read_menu == '2':
                        cari_matkul = input("Masukkan nama mata kuliah yang dicari dari transkrip akademik: ").title()
                        show_1_row(cari_matkul)
                    elif read_menu == '3':
                        break
                    elif read_menu == '4':
                        end_mahasiswa()
                        exit()
                    else:
                        invalid_input()
                    
            elif menu == '2':
                while True:
                    krs_menu__mahasiswa()
                    krs_menu = input("Masukkan angka menu yang ingin dijalankan: ")
                    if krs_menu == '1':
                        krs_table()
                    elif krs_menu == '2':
                        krs_pilihan_table()
                    elif krs_menu == '3':
                        break
                    elif krs_menu == '4':
                        end_mahasiswa()
                        exit()
                    else:
                        invalid_input()
                    
            elif menu == '3':
                kks_menu_mahasiswa()
                kks_menu = input("Masukkan angka menu yang ingin dijalankan: ")
                if kks_menu == '1':
                    while True:
                        kks_table()
                        jumlah_sks = 0
                        for i in range(len(transkrip)):
                            jumlah_sks+=transkrip[i][head_transkrip.index("Sks")]
                        
                        list_nilai = []
                        for i in range(len(transkrip)):
                            total_nilai = transkrip[i][head_transkrip.index("Nilai")] * transkrip[i][head_transkrip.index("Sks")]
                            list_nilai.append(total_nilai)
                            
                        jumlah_nilai = 0
                        for j in list_nilai:
                            jumlah_nilai += j

                        print("Indeks Prestasi Kulmulatif (IPK):")
                        print(round(jumlah_nilai/jumlah_sks,2))
                        break
                    
                if kks_menu == '2':
                    break
                if kks_menu == '3':
                    end_mahasiswa()
                    exit()
                else:
                    invalid_input()
            
            elif menu == '4':
                end_mahasiswa()
                exit()
                
            elif menu == '5':
                break
                
    else:
        invalid_input()     


