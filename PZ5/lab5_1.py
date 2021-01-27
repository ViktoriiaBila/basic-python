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

clean_list([1, 1.0, '1', -1, 1])
clean_list(['qwe', 'reg', 'qwe', 'REG'])
clean_list([32, 32.1, 32.0, -123])
clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])