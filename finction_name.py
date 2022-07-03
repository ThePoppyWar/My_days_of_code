def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Result: {f_name} {l_name}"


print(format_name(input("What's your first name?"), input("What's your last name?")))
