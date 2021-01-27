import sys
string=str(sys.argv[1]).lower().replace(' ','')
list_string=list(string)
list_string_r=list(string)
list_string_r.reverse()
if list_string==list_string_r:
    print ('YES')
else:
    print ('NO')
