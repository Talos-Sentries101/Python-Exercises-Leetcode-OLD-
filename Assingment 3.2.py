hrs= input('Enter no.of hours:')
fhrs= float(hrs)
rt= input('Enter no.of rate:')
frt= float(rt)
if fhrs<=40:
       x= fhrs*frt
if fhrs>40:
    y= 40*frt
    xx= fhrs-40
    yy= xx*(frt*1.5)
    x= y+yy
print(x)
