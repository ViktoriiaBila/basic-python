'''
Розробити функцію encode_morze(text),
яка приймає 1 аргумент -- рядок,
та повертає рядок, який містить діаграму сигналу, що відповідає переданому тексту, 
закодованому міжнародним кодом Морзе для англійського алфавіту. 
Розділові та інші знаки, що не входять до латинського алфавіту, ігнорувати. 
Регістром літер нехтувати.
'''
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

def encode_morze(text):
    l_text = list(text.upper())
    
    #deletion punctustion from text
    l_text_without_punctustion = []
    for i in range(len(l_text)):
        if l_text[i] in morse_code.keys():
            l_text_without_punctustion.append(l_text[i])
        elif l_text[i] == " ":
            l_text_without_punctustion.append(l_text[i])
    
    #conversion letters to signs of morse_code
    l_text_cm = []
    for i in range(len(l_text_without_punctustion)):
        l_text_cm.append(morse_code.get(l_text_without_punctustion[i], " "))
    print (l_text_cm)
    
    #conversion signs of morse_code to signs of signal_diagram
    text_sd = ''
    for i in range(len(l_text_cm)):
        for j in range(len(list(l_text_cm[i]))):
            if l_text_cm[i][j] == ".":
                text_sd = text_sd + "^"
            elif l_text_cm[i][j] == "-":
                text_sd = text_sd + "^"*3
            else:
                text_sd = text_sd +"_"
            if (j+1) != len(l_text_cm[i]):
                text_sd = text_sd +"_"
        if (i+1) != len(l_text_cm):
            text_sd = text_sd +"_"*3
    return (text_sd)


print (encode_morze('Joric is a good boy!'))

