def computepay(hrs,rt):
 if hrs<=40:
        x= hrs*rt
 if hrs>40:
     y= 40*rt
     xx= hrs-40
     yy= xx*(rt*1.5)
     x= y+yy
 return x
hrs = float(input("Enter Hours:"))
rt= float(input('Enter rate:'))
p = computepay(hrs,rt)
print("Pay",p)
