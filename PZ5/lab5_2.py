def counter(a,b):
    def clean_list(list_to_clean):
        for i in range(len(list_to_clean)-1):
            j=1
            while j < len(list_to_clean):
                if j+i < len(list_to_clean):
                    if list_to_clean[i] == list_to_clean[j+i] and type(list_to_clean[i]) == type(list_to_clean[j+i]):
                        el = list_to_clean.pop(j+i)
                    else:
                        j += 1
                else:
                    break
        return (list_to_clean)    
    
    list_a = list(str(a))
    list_b_new = clean_list(list(str(b)))
    
    result = 0
    
    for i in  range(len(list_b_new)):
        j=0
        while j < (len(list_a)):
            if list_b_new[i] == list_a[j]:
                result += 1
                break
            else:
                j += 1

    return (result)

n1 = input ('a=')
n2 = input ('b=')

res = counter(n1, n2)
 
print (str(res))