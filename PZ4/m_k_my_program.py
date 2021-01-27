import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
"""
coded_text_first=sys.argv[1].replace(' ','')
coded_text=''
text_ab=''
text_result=''
"""
coded_text=''
text_result_new=''
text_finish=''
number=0

key=str(input('Please, input your string key: ')).lower()
text=str(input('Please, input your message: ')).replace(' ','').lower()

for t in range(len(text)):
    for a in range(len(alphabet)):
        if text[t]==alphabet[a]:
            coded_text=coded_text+key[a:a+5]
            break

text_result=str(input('Please, input text, which has length equal '+str(len(coded_text))+': ')).replace(' ','').lower()

for i in range(len(coded_text)):
    text_result_new=text_result_new+text_result[i]

for i in range(len(text_result_new)):
    if coded_text[i]=='b':
        text_finish=text_finish+text_result_new[i].upper()
    else:
        text_finish=text_finish+text_result_new[i]

print (text_finish)
