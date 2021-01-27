def file_search(folder,filename):
    result = ''
    p = ''
    f = folder
    file = filename
    def file_s(f,file,result,p):
        #result = result + f[0]
        for i in range(len(f)):
            #result = result + f[0]
            print ('result after for=',result)
            print ('---------')
            print ('name folder',f[0])
            print ('i=',i)
            print ('p=',p)
            if isinstance(f[i],list):
                result = file_s(f[i],file,result,p)
                p = p + f[0] + '/' 
                print ('result if=',result)
            elif f[i] == file:
                result = result + f[0] + '/' + f[i]
                print ('result elif=',result)
        return (result)
            #else:
                #result = result.replace(f[0],'',1)
                #print ('result after del=',result)
    return (file_s(folder,filename,result,p))    

print (file_search(['C:',['P1','e_1','e_2'],['P2',['P3','e','t'],'u'],'e_3','e_4'],'e'))