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
    text_list_without_space = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').lower().split()

    

    result = []
    d = {}
    for j in range(len(text_list_without_space)):
        count = 0
        for i in range(len(text_list_without_space)):
            if text_list_without_space[j] == text_list_without_space[i]:
                count = count + 1
        d[text_list_without_space[j]] = count
    print (d)
    for word in d:
        print (word)
    return (sorted(result))
  


print (find_most_frequent('Mike-Paul   hhh  h mike...'))
#print (find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello"))
#print (find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind") )
#print (find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.') )
'''

def find_most_frequent(text):
    # якщо текст порожній - нема чого шукати
    if text == '':
        return []
    # видаляємо розділові знаки, змінюємо регістр та перетворюємо рядок у список слів
    text_list = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').lower().split()
    # створюємо словник, де для кожного унікального слова зберігатимемо кількість його входжень.
    counts = dict()
    word = ''
    # для кожного слова в списку
    for word in text_list:
        # якщо воно вже присутнє у словнику
        if word in counts:
            # збільшуємо його лічильник на 1
            counts[word] = counts[word] + 1
        else:
            # інакше додаємо у словник
            counts[word] = 1

    # беремо останнє оброблене слово і вважаємо його найчастіше вживаним
    max_word = [word]
    # перевіряємо слова условнику, шукаючи слово із найбільшим лічильником
    for word in counts:
        # якщо знаходиме частіше вживане слово, зберігаємо його як єдиний елемент списка "лідерів"
        if counts[word] > counts[max_word[0]]:
            max_word = [word]
        # якщо знаходимо слово з аналогічною вживаністю, додаємо у список
        elif counts[word] == counts[max_word[0]] and word != max_word[0]:
            max_word.append(word)
    # повертаємо список слів-"лідерів"
    return max_word
    '''