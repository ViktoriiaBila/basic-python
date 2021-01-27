import sys
import math
n=int(sys.argv[1])
i=0
pprevious=0
previous=1
current=0
if n<0:
    print (str(n)+' is not a positive number')
else:
    if n==0:
        print (str(0))
    else:
        if n==1:
            print (str(1))
        else:
            for i in range (n-1):
                current=pprevious+previous
                pprevious=previous
                previous=current
            print (str(current))
        
