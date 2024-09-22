fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
text = line
q= text.find('')
ti=text[q:23]
t=str(ti)
for i in t:
    print(i)
