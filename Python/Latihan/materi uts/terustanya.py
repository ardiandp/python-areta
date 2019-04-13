terus_tanya = True
while terus_tanya :
    temp = input('Masukan Angka Kurang Dari 10 :')
    angka = int(temp)
   
    if angka < 10:
        terus_tanya = False
        print ("anda menginput nilai ",angka)
    else:
        terus_tanya = True
