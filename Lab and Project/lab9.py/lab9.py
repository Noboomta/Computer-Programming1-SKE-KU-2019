def dic1(n):
    ''' return the dict which have a square of keys to be a values
    
    >>> dic1(9)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    
    >>> dic1(3)
    {1: 1, 2: 4, 3: 9}
    
    >>> dic1(2)
    {1: 1, 2: 4}
    
    >>> dic1(1)
    {1: 1}
    
    >>> dic1(5)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    
    '''
    d = dict()
    for i in range(n):
        d[i+1] = (i+1)**2
    return d

def dic2(keya,valuea):
    """ return dict which combine 2 dicts
    
    >>> dic2([1,2,3],['11212','sasa','sdaww'])
    {1: '11212', 2: 'sasa', 3: 'sdaww'}
    
    >>> dic2(['s','a','b'],['11212','sas','sdaw'])
    {'s': '11212', 'a': 'sas', 'b': 'sdaw'}
    
    >>> dic2([1,'as',2,'boom'],['boom','gas','to',101])
    {1: 'boom', 'as': 'gas', 2: 'to', 'boom': 101}
    
    """
    new_dic = dict()
    for index,value in enumerate(keya):
        new_dic[keya[index]] = valuea[index]
    return new_dic

def max_min(dictt):
    ''' function which returns max and min value
    
    >>> max_min({'x':500, 'y':5874, 'z': 560})
    Maximum Value: 5874
    Minimum Value: 500
    
    >>> max_min({'dog':4, 'cat':5, 'ant': 6})
    Maximum Value: 6
    Minimum Value: 4
    
    >>> max_min({'a':4, 'b':50, 'c': 6 , 'd':40 , 'e': -1})
    Maximum Value: 50
    Minimum Value: -1
    
    '''
    new_list = []
    for i in dictt.values():
        new_list.append(i)
    new_list.sort()
    print(f"Maximum Value: {new_list[-1]}\nMinimum Value: {new_list[0]}")

def d1_d2(d2,d1):
    ''' function return the comebine of 2dicts
    
    >>> d1 = {'a': 100, 'b': 200, 'c':300}
    >>> d2 = {'a': 300, 'b': 200, 'd':400}
    >>> d1_d2(d1,d2)
    {'a': 400, 'b': 400, 'd': 400, 'c': 300}
    
    >>> a = {'ant': 100, 'dog': 200}
    >>> b = {'ant': 10, 'dog': 50}
    >>> d1_d2(a,b)
    {'ant': 110, 'dog': 250}
    
    >>> boom = {'boom_brain_iq': 180}
    >>> cat = {'cat_brain_iq': 100}
    >>> d1_d2(boom,cat)
    {'cat_brain_iq': 100, 'boom_brain_iq': 180}
    
    '''
    dic = {}
    for key in d1:
        if key in d2:
            dic[key] = d1[key]+d2[key]
        else:
            dic[key] = d1[key]
    for key in d2:
        if key not in dic:
            dic[key] = d2[key]
    return dic

def three_max(my_dict):
    ''' function find key of 3 max value,return by list
    
    >>> three_max({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}) 
    ['e', 'b', 'c']
    
    >>> three_max({'ant':6,'dog':4,'spider':8,'human':2,'bird':2})
    ['spider', 'ant', 'dog']
    
    >>> three_max({'art':6,'sci':4,'math':8,'econ':2,'pe':2})
    ['math', 'art', 'sci']
    
    '''
    list_value = []
    a_list = []
    blank_list = []
    for i in  my_dict:
        list_value.append(my_dict[i])
        a_list.append([my_dict[i],i])
    list_value.sort()
    for i in list_value:
        for index,value in enumerate(a_list):
            if i == a_list[index][0] and a_list[index][1] not in blank_list:
                blank_list.append(a_list[index][1])
    blank_list = blank_list[-3:]
    blank_list.reverse()
    print(blank_list)

def list_in_dict(dic):
    ''' return the amount of list in value in dict
    
    >>> list_in_dict({'Alex': ['subj1', 'subj2', 'subj3'], 'Tom':2 ,'David': ['subj1', 'subj2']})
    5
    
    >>> list_in_dict({'a':[1,2,3],'b':[1,2],'c':1})
    5
    
    >>> list_in_dict({'dog':['a',22],'sssssssw':[11,21]})
    4
    
    '''
    count = 0
    for i in dic.values():
        if type(i) == list:
            count += len(i)
    print(count)
