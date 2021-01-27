import sys
list_new=''
list_inp=sys.argv[1:]

list_inp.reverse()
list_inp_length=len(list_inp)

list_new=list_new+str(list_inp[0])

for i in range(list_inp_length-1):
    list_new=list_new+' '+str(list_inp[i+1])
print (list_new)
