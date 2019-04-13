def cetak_biodata(nama,kota,umur=18):
    print ("Nama :",nama);
    print ("Umur :",umur);
    print ("Kota :",kota);
    return;

#kalau parameter di isi semua
print ("Tanpa memakai default Argument")
cetak_biodata(Nama="Miki",umur=50,kota="Bandung")

print("/n/n")

#kalau parameter tidak di isi semua
print ("memakai default Argument")
cetak_biodata(Nama="Budi",kota="Bandung")
