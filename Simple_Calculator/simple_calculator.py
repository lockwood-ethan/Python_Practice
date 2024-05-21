cont_calc = "n"
while cont_calc == "n":
    first_num = float(input("What's the first number? "))
    cont_calc = "y"
    while cont_calc == "y":
        operand_dict = {"+": lambda first_num, second_num: first_num + second_num,
                        "-": lambda first_num, second_num: first_num - second_num,
                        "*": lambda first_num, second_num: first_num * second_num,
                        "/": lambda first_num, second_num: first_num / second_num
        }
        for key in operand_dict.keys():
            print(key)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number? "))
        if operation == "+":
            result = operand_dict["+"](first_num, second_num)
        elif operation == "-":
            result = operand_dict["-"](first_num, second_num)
        elif operation == "*":
            result = operand_dict["*"](first_num, second_num)
        elif operation == "/":
            result = operand_dict["/"](first_num, second_num)
        else:
            print("Incorrect operation entered")
            break
        print(f"{first_num} {operation} {second_num} = {result}")
        first_num = result
        cont_calc = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")