'''
Розробити функцію convert_n_to_m(x, n, m),
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке
число, та цілі числа n та m (1 <= n, m <= 36), та 
повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, або не може бути представленням цілого невід'ємного 
числа в системі числення з основою n, повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 
використовувати літери латинського алфавіту у верхньому регістрі від A до Z. 
У вхідному x можуть використовуватися обидва регістри.

Вважати, що в одиничній системі числення число записується відповідною кількістю нулів.
'''

def convert_n_to_m(x, n, m):
    dict_numbers = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
    dict_letters = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
    
    #checking the type of x 
    if isinstance(x,(str,int,long)):
        x = str(x)
    else:
        return (False)  
    
    x = x.upper()
    
    #if the type of x is the long, then delete last 'L'
    if x[-1] == 'L' and n == 10:
        x = x[:-1]  
    
    #if x consists a numeral greater than or equal to n
    for k in range(len(x)):
        if dict_numbers[x[k]] >= n:
            return (False)
    
    #convert x_n to y_10 (n=1)
    if n == 1:
        y_10 = len(x)
    else:        
        #convert x_n to y_10 (n>=1)
        dict_x_n = {}
        i = len(x)-1
        for j in range(len(x)):
            if x[j] not in dict_numbers.keys():
                dict_x_n[i] = int(x[j])
            else:
                dict_x_n[i] = x[j]
            i -= 1
        print (dict_x_n)
        y_10 = 0
        for key in dict_x_n.keys():
            if dict_x_n[key] not in dict_numbers.keys():
                y_10 += dict_x_n[key] * n**key
            else:
                y_10 += dict_numbers[dict_x_n[key]] * n**key
        
    print ('decimal number = %s'%(y_10))
    
    #convert y_10 to z_m (m=1)
    if m == 1:
        return ('0'*y_10)  
    
    #convert y_10 to z_m (m>=1)
    finish_result = ''
    result_div = y_10
    while result_div >= m:
        remainder_of_div = result_div % m 
        if remainder_of_div >= 10:
            finish_result += dict_letters[remainder_of_div]
        else:
            finish_result += str(remainder_of_div)
        result_div = int(result_div / m)
    if result_div >= 10:
        result_div = dict_letters[result_div]
    return (str(result_div) + finish_result[::-1])
    

print (convert_n_to_m(123123123123123123123, 10, 10))