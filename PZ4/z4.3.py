import sys

count=0
list_=list(sys.argv[1])

for i in range(len(list_)):
    if list_[i]=='(':
        count=count+1
    else:
        count=count-1
    if count<0:
        print ('NO')
        break
if count==0: print ('YES')
elif count>0: print ('NO')

