'''
Розробити функцію count_holes(n),
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа 
друкованими цифрами (вважати, що у "4" та у "0" по одному отвору), 
або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним 
або взагалі не числом.
'''
def count_holes(n):
    count = 0 
    
    def del_0 (s):
        for i in range(len(s)):
            if s[i] not in ['0','-']:
                return (i)

    if isinstance(n,int) == False and isinstance(n,str) == False and isinstance(n,long) == False:
        return ('ERROR')
    
    list_n = list(str(n))
        
    for elem in list_n:
        if elem not in ['-','0','9','8','7','6','5','4','3','2','1']:
            return ('ERROR')
   
    if list_n == ['0']:
        return (1)
    
    list_n_new = [] 
    
    i = del_0(list_n)
    while i < (len(list_n)):
        list_n_new.extend(list_n[i])
        i += 1
    
    for elem in list_n_new:
        if elem in ['9','6','4','0']:
            count += 1
        elif elem == '8':
            count += 2
    return (count) 
  
print (count_holes(111298))
