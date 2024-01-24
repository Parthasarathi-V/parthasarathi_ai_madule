def table(tables, times, name):
    for table in tables:
        if (name == "addition table"):
            for i in range(1, times + 1):        
                print(" {} + {}  =  {}".format(i, table, table+i))

        elif (name == "subtraction table"):
            for i in range(1, times + 1):       
                print(" {} - {}  =  {}".format(i, table, table-i))

        elif (name == "multiplication table" or name == "table"):
            for i in range(1, times + 1):        
                print(" {} × {}  =  {}".format(i, table, table*i))
        
        elif (name == "division table"):
            for i in range(1, times + 1):        
                print(" {} / {}  =  {}".format(i, table, table/i))

        else:
            print("\n***sorry, please check the input***")
        print()



