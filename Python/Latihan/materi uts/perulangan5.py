for num in range(5,15):
        for i in range(2,num):
              if num%i==0:
                       j=num/i
                       print '%d = %d * %d' % (num, i, j)
                       break
        else:
              print (num, ' adalah bilang prima')

print ("selesai")