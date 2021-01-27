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
    print (list_to_clean)