import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
"""
coded_text_first=sys.argv[1].replace(' ','')
coded_text=''
text_ab=''
text_result=''
"""

key=str(raw_input('Please, input your string key:'))
text=str(raw_input('Please, input your message:'))

print (key)
print (text)

"""
for i in range(len(coded_text_first)-len(coded_text_first)%5):
    coded_text=coded_text+coded_text_first[i]
    
for i in range(len(coded_text)):
    if coded_text[i]==coded_text[i].upper():
        text_ab=text_ab+'b'
    else:
        text_ab=text_ab+'a'

for k in range(0,len(text_ab),5):
    for j in range(len(key)):
        if key[j]==text_ab[k] and key[j+1]==text_ab[k+1] and key[j+2]==text_ab[k+2] and key[j+3]==text_ab[k+3] and key[j+4]==text_ab[k+4]:
            text_result=text_result+alphabet[j]
            break

print (text_result)
"""
