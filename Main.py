import calculator
import converter


#declaraction
calc = ['add the', 'sub the', 'mul the', 'div the', 'the pow', 'subtract the', 'multiply the', 'divide the', 'the power']
table = ['addition table', 'subtraction table', 'multiplication table', 'division table']

#inputing statement
query = input("").lower()

for i in calc:
    if i in query:
        print()
        print(calculator.Main(query, converter.for_calc(query)))
        print()  

for i in table:
    if i in query:
        converter.for_table(query, i)   


