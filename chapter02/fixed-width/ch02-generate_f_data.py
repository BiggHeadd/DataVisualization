import string
import random

ROWS = 1000000
#SAMPLE = string.ascii_lowercase
SAMPLE = '012345678901234567890123456'
F1 = 9
F2 = F1 + 13
F3 = F2 + 4

#assert F1 + F2 + F3 == len(SAMPLE)

with open("ch02-fixed-width-1M.data", 'w')as f:
    for r in range(ROWS):
        t = ''.join(random.sample(SAMPLE,len(SAMPLE)))
        print t[0:F1], t[F1:F2], t[F2:F3]
        string = t[0:F1]+" "+t[F1:F2]+" "+t[F2:F3]
        f.write(string+'\n')
