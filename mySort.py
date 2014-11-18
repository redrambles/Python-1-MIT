def mySort(list):
    out = []
    tmp_min = 0
    while len(list) > 0:
        tmp_min = min(list)
        out.append(tmp_min)
        list.remove(tmp_min)    
    return out



##### If list is SORTED - these algorithms can be used to search ###

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


## or (I PREFER THIS ONE!!) ##

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False
