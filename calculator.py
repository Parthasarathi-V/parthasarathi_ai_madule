def Main(query, value):
    
    if len(value) == 0 or value == None :
        values = "Sorry you not give the number, restart the program and Please input the number" 
    
    elif 'add' in query or 'addition' in query:
       print(f"the sum of {value} is  : ",end = '  ')
       values = add(value) 

    elif 'sub' in query or 'subtraction' in query:
        print(f"the subtraction of {value} is  : ",end = '  ')
        values = sub(value)

    elif 'mul' in query or 'multiply' in query or 'multiplication' in query:
        print(f"the multiplication of {value} is  : ",end = '  ')
        values = mul(value)

    elif 'div' in query or 'division' in query:
        print(f"the division of {value} is  : ",end = '  ')
        values = div(value)

    elif 'pow' in query or 'power' in query:
        print(f"the power of {value} is  : ",end = '  ')
        values = pow(value)
    
    else:
        values = "Invalid"
        
    return values

def add(value):
    values = 0
    for i in value:
        values = values + i
    return values

def sub(value):
    values = 0
    for i in value:
        values = value[0] - value[1]
    return values
    
def mul(value):
    values = 1
    for i in value:
        values = values * i
    return values
    
def div(value):
    values = 0
    values = value[0] / value[1]
    return values
    
def pow(value):
    values = 0
    values = value[0] ** value[1]
    return values



