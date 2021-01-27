class Student(object):
    name = None
    mark_lab = None
    mark_exam = None
    f_mark = None
    
    def __init__(self, name, conf = None, mark_lab = [], mark_exam = 0, f_mark = 0):
        self.name = name
        
        self.exam_max = conf['exam_max']
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.k = conf['k']
        
        self.mark_lab = []
        for i in range(self.lab_num):
            self.mark_lab.append(0)
        
        self.mark_exam = mark_exam
        self.f_mark = mark_exam
    
    def make_lab(self,m,n = None):
        if n == None:
            for i in range(len(self.mark_lab)):
                if self.mark_lab[i] == 0:
                    n = i
                    break
        if n == None or n >= self.lab_num:
            return(False)
        if m < self.lab_max:
            self.mark_lab[n] = m
        else:
            self.mark_lab[n] = self.lab_max
        return (self)

    def make_exam(self,m):
        if m < self.exam_max:
            self.mark_exam = m
        else:
            self.mark_exam = self.exam_max
        return (self)
    
    def is_certified(self):
        flag = True
        self.f_mark = self.mark_exam
        for mark in self.mark_lab:
            self.f_mark = self.f_mark + mark
        if self.f_mark/float(self.exam_max+self.lab_max*self.lab_num) < self.k:
            flag = False
        return (self.f_mark,flag)

conf = { 'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61 }

oleg = Student('Oleg', conf)
print (oleg.mark_lab)
oleg.make_lab(1) 
oleg.make_lab(8,0) 
oleg.make_lab(1)
oleg.make_lab(10,7)
oleg.make_lab(4,1) 
oleg.make_lab(5)
oleg.make_lab(6.5)
oleg.make_exam(32) 
print (oleg.mark_lab)
print (oleg.is_certified())
oleg.make_lab(7,1) 
print (oleg.is_certified())

'''
conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o1 = Student('Oleg', conf1)
print (o1.is_certified()) 
o2 = Student('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)
print (o2.is_certified())

o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print (o3.is_certified())
o3.make_lab(20,1).make_lab(20,0)
print (o3.is_certified())
o3.make_lab(50,2)
print (o3.is_certified())
o3.make_lab(40,1)
print (o3.is_certified())


conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print (o4.is_certified())

o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
print (o5.mark_lab)
print (o5.is_certified())
o5.make_lab(7)
print (o5.is_certified())
o5.make_exam(7)


conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print (o6.is_certified())
'''
