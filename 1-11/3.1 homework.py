first_number = int(input())
math_operation = input() #action
second_number = int(input())

if math_operation == "+": result = first_number + second_number
elif math_operation == "-": result = first_number - second_number
elif math_operation == "*": result = first_number *second_number
elif math_operation == "/": result = "Деление на ноль невозможно" if second_number == 0 else first_number / second_number
else: result = ""
print(result)
