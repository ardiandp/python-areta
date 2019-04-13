#penguranpgan
n1 = int(input("Masukkan bilangan pertama: "))
n2 = int(input("Masukkan bilangan kedua: "))
kurang=n1-n2
#print(kurang)
print("Hasil Dari",n1,"-",n2,"Adalah ",kurang)

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif y > 0:
    print("Quadrant II")
else:
    print("Quadrant III")