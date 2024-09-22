fname = input("Enter file name: ")
fh = open(fname, 'r')
o=fh.read()
i=o.upper()
line=i.strip('/n')
for oo in i:
    print(oo)
