import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
if a<=0 or b<=0 or c<=0:
    print ('not triangle')
else:
    if b+c>a and a+b>c and a+c>b:
        print ('triangle')
    else:
        print ('not triangle')
        
