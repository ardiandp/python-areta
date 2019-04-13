def fungsi_tanpa_parameter():
    for i in range(1,5):
        print ("looping ke -",i)

def fungsi_dengan_parameter(batas_akhir):
    for i in range(1,batas_akhir):
        print ("looping ke -",i)

print ("ceontoh penggunaan function tanpa parameter")
print ("hasil:",fungsi_tanpa_parameter())

print ("\n\n")
print ("contoh penggunaan fungsi dengan parameter")
print ("hasil:",fungsi_dengan_parameter(10))

#belum selesai 