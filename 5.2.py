answer = "yes"
while answer == "yes" or answer == "y":
    first_number = int(input())
    math_operation = input()
    second_number = int(input())

    if math_operation == "+":
        result = first_number + second_number
    elif math_operation == "-":
        result = first_number - second_number
    elif math_operation == "*":
        result = first_number * second_number
    elif math_operation == "/":
        result = "Деление на ноль невозможно" if second_number == 0 else first_number / second_number
    else:
        result = ""
    print(result)
    answer = input("Continue? yes/y/no ")




