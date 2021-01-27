'''
def file_search(folder,filename):
    result = ''
    result += folder[0]
    for elem in folder[1::]:
        if type(elem) == type(filename) and elem == filename:
            result = result + '/' + str(elem)
        else:
            if isinstance(elem,list):
                while type(elem) != type(filename):
                    if
'''

'''    
def file_search(folder,filename):
    if isinstance(folder,list):
        print (folder[0])
        file_search(folder[1],filename)
    elif folder == filename:
        print ('/',folder)
    else:
        file_search(folder[2],filename)
        
        for i in range(len(folder)):
            if folder[0] == filename:
                print ('++')
'''

'''
def file_search(folder,filename):
    for i in range(len(folder)):
        print ('name folder',folder[0])
        print ('length folder',str(len(folder)))
        print ('i=',str(i))
        if isinstance(folder[i],str) and folder[i] == filename:
            print ('/',folder[i])
        elif isinstance(folder[i],list):
            return (file_search(folder[i],filename))
'''


def file_search(folder,filename):
    result = False
    path = folder[0]
    for i in range(len(folder)):
        print ('name folder',folder[0])
        print ('i=',str(i))
        print ('file i=',folder[i])
        if isinstance(folder[i],list):
            file_search(folder[i],filename)
        elif folder[i] == filename:
            return (path + '/' + folder[i])


'''
def file_search(folder,filename):
    result = ''
    path = folder[0]
    
    def file_s(folder,filename):
        
        if filename in folder:
            result = path + '/' + filename
            print (result)
        else:
            for i in range(len(folder)):
                if isinstance(folder[i],list):
                    file_s(folder[i],filename)
    
    return (result)
'''

'''
def file_search(folder,filename):
    result = False
    for i in range(len(folder)):
        if folder[i] == filename:
            result = folder[0] + '/' + filename
        elif isinstance(folder[i],list):
            file_search(folder[i],filename)
    return (result)
'''


print (file_search(['C:',['P1'],['P2','e_3','e_4'],'e_5','e_1','e_2'],'e_3'))

#file_search(['C:',['P1',['p1',['e_1_1_1','e_2_1_1'],['p2'],'e_1_1','e_2_1']],['P2'],'el_1','el_2'],'e_2_1')