def calculate():
    first_number = int(input("What's the first number?: "))
    print(" + \n - \n * \n /")
    operate_choice = input("Pick an operation: ")
    next_number = int(input("What's the next number: "))
    if operate_choice == "/":
        result = first_number / next_number
    elif operate_choice == "+":
        result = first_number + next_number
    elif operate_choice == "-":
        result = first_number - next_number
    else:
        result = first_number * next_number
    result_2 = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if result_2 == "no":
    return


calculate()

