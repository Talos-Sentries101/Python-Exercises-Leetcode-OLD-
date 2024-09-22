text = "X-DSPAM-Confidence:    0.8475"
q= text.find('    ')
ti=text[q:31]
t=float(ti)
print(t)
