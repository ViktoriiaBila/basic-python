'''
Розробити функцію find_most_frequent(text),
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, 
пробіли та розділові знаки (,.:;!?-);
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). 
Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") 
вважаються різними словами. 
Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.
'''

def find_most_frequent(text):
    text = text.lower() + '.'
    
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    
    text_list = []
    text_elem = ''
    for i in range(len(text)):
        if text[i] in alphabet:
            text_elem = text_elem + text[i]
        else:
            text_list.append(text_elem)
            text_elem = ''    
    
    
    text_list_without_space = []
    for elem in text_list:
        if elem != '':
            text_list_without_space.append(elem)
    #print (text_list_without_space)
    
    result = []
    d = {}
    for j in range(len(text_list_without_space)):
        count = 0
        for i in range(len(text_list_without_space)):
            if text_list_without_space[j] == text_list_without_space[i]:
                count = count + 1
        d[text_list_without_space[j]] = count
    #print (d)
    
    quantity_most_frequent = max(d.values())
    for word in text_list_without_space:
        if d[word] == quantity_most_frequent and word not in result:
            result.append(word)
    return (sorted(result))
    


#print (find_most_frequent('Mike-Paul mike'))
#print (find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello"))
#print (find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind") )
print (find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.') )


