import sys
import math
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
if z==1:
    print ('Everybody sing a song:'+(' '+'la-'*(x-1)+'la')*y+'!')
else:
    print ('Everybody sing a song:'+(' '+'la-'*(x-1)+'la')*y+'.')
