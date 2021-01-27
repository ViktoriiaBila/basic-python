import sys
list_inp=sys.argv[1:]

list_inp.reverse()

list_new=list_inp[0]

for i in list_inp[1:]:
    list_new=list_new+' '+i
print (list_new)
