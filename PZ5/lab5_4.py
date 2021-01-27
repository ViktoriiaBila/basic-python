def file_search(folder,filename):
    p = folder[0] + '/'
    if filename in folder:
        return (p + filename)
    else:
        for elem in folder:
            p = folder[0] + '/'
            if isinstance(elem,list):
                result = file_search(elem,filename)
                if result:
                    return (p + result)
    return (False)
