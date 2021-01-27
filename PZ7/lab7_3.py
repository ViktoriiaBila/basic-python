class SuperStr(str):
    a = None
    
    def __init__(self, a = ''):
        self.a = a    
    
    def is_repeatance(self, s):
        flag = False
        if type(s) == str and s != '' and float(len(self.a))%float(len(s)) == 0:
            for i in range(int(len(self.a)/len(s))):
                if self.a == s*(i+1):
                    flag = True  
        return (flag)    
    
    def is_palindrom(self):
        flag = True
        b = self.a.lower()
        for i in range(int(len(b)/2)):
            if b[i]==b[-(i+1)]:
                flag = True
            else: 
                flag = False
                break
        return (flag)

s = SuperStr('123123123123')
print (s.is_repeatance('123')) # True
print (s.is_repeatance('123123')) # True
print (s.is_repeatance('123123123123')) # True
print (s.is_repeatance('12312')) # False
print (s.is_repeatance(123)) # False
print (s.is_palindrom()) # False
print (s) # 123123123123 (рядок)
print (int(s)) # 123123123123 (ціле число)
print (s + 'qwe') # 123123123123qwe

p = SuperStr('123_321')
print (p.is_palindrom()) # True

s2 = SuperStr('9')
print (s2.is_palindrom())
'''
s1 = SuperStr('678678678678')
print (s1.is_repeatance('6786'))
print (s1.is_repeatance('678'))
print (s1.is_repeatance('678678'))
print (s1.is_repeatance('678678678'))
print (s1.is_repeatance('q'))
print (s1.is_repeatance(''))
print (s1.is_repeatance(678))
print (s1.is_repeatance([]))
print (s1.is_repeatance([678]))
print (s1.is_palindrom())
print (s1.isdigit())
print (int(s1))
print ('("' + s1 + '")')

s2 = SuperStr('')
print (s2.is_repeatance(''))
print (s2.is_repeatance('a'))
print (s2.is_palindrom())
print (bool(s2))

s3 = SuperStr('mystring1Gnirtsym')
print (s3.is_repeatance('my'))
print (s3.is_repeatance('q,.%;#'))
print (s3.is_palindrom())
print (s3.lower())
print (s3)

s4 = SuperStr('q')
print (s4.is_repeatance(''))
print (s4.is_repeatance('q'))
print (s4.is_palindrom())
print (s4.upper()) 
'''