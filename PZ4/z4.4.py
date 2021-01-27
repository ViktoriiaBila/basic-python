import sys
count=0

number1=int(sys.argv[1])
number2=int(sys.argv[2])

range_of_numbers=list(range(number1,number2+1))

for item in range_of_numbers:
    summ_first=0
    summ_last=0

    str_item=str(item)

    for i in str_item[:-3]:
        summ_first=summ_first+int(i)
    
    for i in str_item[:-4:-1]:
        summ_last=summ_last+int(i)
    
    if summ_first==summ_last:
        count=count+1

print (str(count))
