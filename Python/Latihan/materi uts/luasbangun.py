print ('==========')
print ('program mencari luas-luas bangun datar')
print ('==========')

def luas_persegi() :
    print (' ' )
    print ('program mencari luas persegi')
    x= float(input ('panjang sisi : '))
    luasp= x*x
    print (' ')
    print ('luas perseginya adalah : ' , luasp , 'cm2')

def luas_pp () :
    print (' ' )
    print ('program mencari luas persegi panjang')
    print (' ')
    x= float(input('masukkan panjangnya : '))
    print (' ' )
    y= float(input ('masukkan lebarnya : '))
    c = x*y
    print (' ' )
    print ('luas persegi panjangnya adalah : ' , c , 'cm2')

def luas_segitiga () :
    print (' ' )
    print ('program mencari luas segitiga' )
    print (' ')
    x= float(input('masukkan alas segitiga : '))
    y= float(input('masukkan tinggi segitiga :'))
    a=0.5*x*y
    print (' ' )
    print ('luas segitiganya adalah : ' , a, 'cm2')
    
def luas_lingkaran () :
    print (' ' )
    print (' program mencari luas lingkaran ')
    print (' ')
    x = float(input('masukkan jari-jari lingkaran : '))
    luas = 22/7*x*x
    print ('')
    print ('luas lingkarannya adalah : ' , luas , 'cm2')
              
def luas_jg () :
    print (' ' )
    print (' program mencari luas jajaran genjang ')
    print (' ')
    x= float(input('masukkan tinggi jajaran genjang : '))
    y= float (input('masukkan alas jajaran genjang :' ))
    luas = x*y
    print ('')
    print ('luas jajaran genjang adalah : ' , luas , 'cm2')

def luas_trapesium () :
    print (' ' )
    print (' program mencari luas trapesium ')
    print (' ')
    x= float (input('masukkan sisi atas trapesium : '))
    y= float(input('masukkan sisi bawah trapesium : '))
    z= float (input('masukkan tinggi trapesium : '))
    luas = (x+y)*z/2
    print ('')
    print ('luas trapesiumnya adalah : ' , luas, 'cm2')
             
def luas_bk () :
    print (' ' )
    print (' program mencari luas belah ketupat ')
    print (' ')
    x= float(input('masukkan diagonal 1 : '))
    y= float(input('masukkan diagonal 2 : ' ))
    luas = 0.5*x*y
    print ('')
    print ('luas belah ketupatnya adalah : ', luas, 'cm2')