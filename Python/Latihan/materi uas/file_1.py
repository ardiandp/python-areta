try:
    sebuah_file=open("absen.txt",'w')

    print("Nama File yang dibuat: ",sebuah_file.name)
    print("Mode Pembacaan File: ",sebuah_file,mode)
    print("Apakah filenya sudah di tutup: ", sebuah_file.closed)

    sebuah_file.close()
    print("apakah filnay sudah di tutup: ?",sebuah_file.closed)
    except IOError,e;
    print("Prigres gagal karea",e)