number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#it is used only for calculator sometimes only  using other    
def for_calc(query):
    
    #declarations
    val1 = []
    #excute
    splited = query.split()
    for i in range(len(splited)):
        value = ''
        x = 0
        for word in splited[i]:
            if word in number_list:
                value = value + word
        if value != '':
            val1.append(int(value))
    return val1;

import tables

def for_table(query, name):
    pos = []
    query = query.split()
    for i in range(len(query)):
        for letter in query[i]:
            if letter in number_list:
                pos.append(int(i))  

    ext = ['st', 'nd', 'rd', 'th', ',']
    pos = set(pos)
    table = []
    times = 10

    for i in pos:
        if query[i-1] == 'upto':
            times = int(query[i])
        
        elif len(query)-1 > i:
            if query[i+1] == "and" or query[i-1] == "and":
                table = [int(query[i]) for i in pos]
        
        for ex in ext:
            if ex in query[i]: 
                table.append(int(query[i].replace(f'{ex}', '')))
        
    tables.table(table, times, name)
