import sys
import math
x=float(sys.argv[1])
y=float(sys.argv[2])
z=float(sys.argv[3])
print (1/(z*math.sqrt(2*math.pi))*math.pow(math.e,(y-x)*(x-y)/2/z/z))
