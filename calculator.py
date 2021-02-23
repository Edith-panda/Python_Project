# calculator
def add(number_1 , number_2):
    return number_1 + number_2
def subtract(number_1 , number_2):
    return number_1 - number_2
def multiply(number_1 , number_2):
    return number_1 + number_2
def divide(number_1 , number_2):
    return number_1 + number_2

print("please select opreation as -\n" \
"1. add \n"
"2. subtract\n"
"3. multiply\n"
"4. divide\n")
select = int(input("select operation amoung 1 for add , 2 for subtract , 3 for multiply, 4 for divide"))

number_1 = input("enter your first number")
number_2 = input("enter second number ")


if select == 1 :
    print(number_1, "+", number_2, "=", add(number_1,number_2))
elif select == 2 :
    print(number_1, "-", number_2, "=", subtract(number_1,number_2))
elif select == 3 :
    print(number_1, "*", number_2, "=", multiply(number_1,number_2))
elif select == 4 :
    print(number_1, "/", number_2, "=", divide(number_1,number_2))
else:
    print("invalid input")
    
