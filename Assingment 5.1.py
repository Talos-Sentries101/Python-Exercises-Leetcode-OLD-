largest =None
smallest = None
while True:
    num=input('Enter a number:' )
    if num == 'done' :
        break
    try:
        fnum=int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=fnum
    if fnum > largest:
        largest=fnum
    if smallest==None:
        smallest=fnum
    if fnum < smallest:
        smallest=fnum

print("Maximum is", largest)
print("Minimum is", smallest)
