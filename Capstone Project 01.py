dataNilai={}

def menuProgram():
    print('\t\t=======================================================')
    print("\t\t\t\tSELAMAT DATANG DI PROGRAM")
    print("\t\t\t\t  DATA NILAI MAHASISWA")
    print("\t\t=======================================================")

    print(f"\t\t1. Tampilkan Data Nilai Mahasiswa")
    print(f"\t\t2. Tambahkan Data Nilai Mahasiswa")
    print(f"\t\t3. Perbarui Data Nilai Mahasiswa")
    print(f"\t\t4. Hapus Data Nilai Mahasiswa")
    print(f"\t\t5. Keluar Program\n")

    print("\t\t=======================================================\n")

def tambahData():
    while True:
        print('\n\t\t=======================================================')
        print("\t\t\t      Menu Tambah Data Mahasiswa")
        print('\t\t=======================================================')
        print("\t\t1. Tambah Data Nilai Siswa")
        print("\t\t2. Kembali Ke Menu Utama")
        print('\t\t=======================================================\n')
        menuTambah = input('\t\tSilahkan Pilih Menu [1-2]: ')
        
        if menuTambah == '1':
            primKey = int(input('\n\t\tMasukan NIM\t\t\t: '))
            if primKey in dataNilai:
                print('\n\t\t*****Data Nilai Mahasiswa Telah Tersedia*****')
            else:
                nama = input('\t\tMasukan Nama Mahasiswa\t\t: ')
                prodi = input('\t\tMasukan Program Studi Mahasiswa\t: ')
                matakuliah = input('\t\tMasukan Mata Kuliah\t\t: ')
                nilaiuts = input('\t\tMasukan nilai UTS\t\t: ')
                nilaiuas = input('\t\tMasukan nilai UAS\t\t: ')
                
                dataSementara = {'nama':{nama}, 'prodi':{prodi}, 'matakuliah':{matakuliah}, 'nilaiuts':{nilaiuts}, 'nilaiuas':{nilaiuas}}    

                yakin='a'
                while (yakin != 'N' or yakin !='n'):
                    yakin = input("\t\tApakah Data Akan Disimpan? (Y/N): ")
                    if(yakin=='y' or yakin=='Y'):
                        dataNilai.update({primKey : dataSementara}) 
                        print("\n\t\t*****Data Tersimpan*****")
                        break
                    if (yakin == 'N' or yakin == 'n'):
                        print('\n\t\t*****Data Anda Tidak Tersimpan*****')
                        break    
        elif menuTambah == '2': 
            break                         
        else:
            tambahData()
            break            
           
def tampilData():
    while True:
        print('\n\t\t=======================================================')
        print('\t\t\t     Menu Tampil Data Nilai Mahasiswa')
        print('\t\t=======================================================')
        print('\t\t1. Tampilkan semua Data Nilai Mahasiswa')
        print('\t\t2. Tampilkan Data Nilai Mahasiswa Sesuai Dengan NIM')
        print('\t\t3. Kembali Ke Menu Utama')
        print('\t\t=======================================================')
        menuTampil = input('\t\tSilahkan Pilih Menu [1-3]: ')
        
        if menuTampil == '1':
            if(len(dataNilai)>0):
                i = 0
                for nim, mahasiswa in dataNilai.items():
                    print("\t\t %d. NIM : %s, Nama : %s,  : %s, matakuliah : %s, nilaiuts : %s, nilaiuas : %s" %(i+1,nim,mahasiswa['nama'],mahasiswa['prodi'],mahasiswa['matakuliah'],mahasiswa['nilaiuts'],mahasiswa['nilaiuas']))
                    tampilData()
                break 
            else:
                print("\n\t\t******Tidak Ada Data Nilai Mahasiswa*****")
                tampilData()
            break
        elif menuTampil == '2':
            nim = int(input('\n\t\tMasukan NIM\t: '))
            if nim in dataNilai:
                print('\t\tData Nilai Mahasiswa Dengan NIM', nim)
                print("\t\tNIM : %s, Nama : %s,  : %s, matakuliah : %s, nilaiuts : %s, nilaiuas : %s" %(nim,dataNilai[nim]['nama'],dataNilai[nim]['prodi'],dataNilai[nim]['matakuliah'],dataNilai[nim]['nilaiuts'],dataNilai[nim]['nilaiuas']))
                tampilData()
                break   
            else:
                print('\n\t\t*****Data Mahasiswa Tidak Ditemukan*****')
                tampilData()
            break
        
        elif menuTampil == '3': 
            break
        
        else:
            tampilData()
        break

def ubahData():
    while True:
        print('\n\t\t=======================================================')
        print('\t\t\t     Menu Update Data Nilai Mahasiswa')
        print('\t\t=======================================================')
        print('\t\t1. Ubah Data Nilai Mahasiswa')
        print('\t\t2. Kembali Ke Menu Utama')
        print('\t\t=======================================================')
        ubahData = input('\t\tSilahkan Pilih Menu [1-2]: ')
        
        if ubahData == '1':

            primKey = int(input('\t\tMasukan NIM\t: '))
            if primKey in dataNilai:
                print('\t\tMahasiswa Dengan NIM', + primKey)
                print("\t\tnim : %s, nama : %s, prodi : %s, matakuliah : %s, nilaiuts : %s, nilaiuas : %s" %(primKey,dataNilai[primKey]['nama'],dataNilai[primKey]['prodi'],dataNilai[primKey]['matakuliah'],dataNilai[primKey]['nilaiuts'],dataNilai[primKey]['nilaiuas']))

                yakin = 'a'
                while (yakin != 'N' or yakin != 'n'):
                    yakin = input('\t\tApakah Anda Yakin Ingin Mengubah Data Mahasiswa (Y/N): ')
                        
                    if (yakin == 'Y' or yakin == 'y' ):
                        gantiData = input('\t\tMasukan Data yang Akan Diubah\t: ')
                        if gantiData in dataNilai[primKey]:
                            dataBaru = input('\t\tMasukan Data %s Baru\t\t: '%gantiData)
                            konfirmasiUpdate = 'a'
                            while (konfirmasiUpdate != 'n' or konfirmasiUpdate != 'N'):
                                konfirmasiUpdate = input('\t\tApakah Anda Yakin ingin Merubah Data %s (Y/N)\t: '%gantiData)
                                if (konfirmasiUpdate == 'y' or konfirmasiUpdate == 'Y'):
                                    dataNilai[primKey][gantiData] = dataBaru
                                    print('\n\t\t*****Data Anda Berhasil Dirubah*****') 
                                    break
                                elif (konfirmasiUpdate == 'N' or konfirmasiUpdate == 'n'):
                                        print('\n\t\t*****Data Gagal Dirubah*****') 
                                break
                                            
                        else:
                            print('\n\t\t*****Data yang Anda Masukan Tidak Sesuai*****')
                        break
                    
                    elif (yakin == 'N' or yakin == 'n'):
                        print('\n\t\t*****Data Tidak Jadi Dirubah*****') 
                    break                
            else:
                print('\n\t\t*****Data Mahasiswa Tidak Ditemukan*****')    
        
        elif ubahData == '2':
            break
        
    
def hapusData():
    while True:
        print('\n\t\t=======================================================')
        print('\t\t\t     Menu Hapus Data Nilai Mahasiswa')
        print('\t\t=======================================================')
        print('\t\t1. Hapus Data Nilai Mahasiswa')
        print('\t\t2. Kembali Ke Menu Utama')
        print('\t\t=======================================================')        
        hapusData = input('\t\tSilahkan Pilih Menu [1-2]: ')
        
        if hapusData == '1':
            
            primKey = int(input('\n\t\tMasukan NIM\t: '))
            if primKey in dataNilai:
                
                yakin = 'a'
                while (yakin != 'N' or yakin != 'n'):
                    yakin = input('\t\tApakah Anda Yakin Ingin Menghapus Data Dengan NIM %s (Y/N)?: '%primKey)
                    if (yakin == 'Y' or yakin == 'y'):
                        del dataNilai[primKey]
                        print('\n\t\t*****Data Berhasil Dihapus*****')
                        break
                    elif (yakin == 'n' or yakin == 'N'):
                        print('\n\t\t*****Data Gagal Dihapus*****')
                    break
            else:
                print('\n\t\t*****Data Mahasiswa Tidak Ditemukan*****')   
       
        elif hapusData == '2': 
            break  

while True:
    menuProgram()
    pilihan_menu = input("\t\tSilahkan Pilih Opsi [1-5]: ")
    
    if pilihan_menu == '1':
        tampilData()
    elif pilihan_menu == '2':
        tambahData()
    elif pilihan_menu == '3':
        ubahData()
    elif pilihan_menu == '4':
        hapusData()
    elif pilihan_menu == '5':
        print('\n\t\t\t-----Program Selesai-----\n\t\t\t -----Terima Kasih-----') 
        break
    else:
        print('\n\t\t*****Pilihan yang Anda Masukan Salah*****\n')
    
        