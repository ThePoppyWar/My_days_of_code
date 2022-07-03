def format_name(f_name, l_name):
    '''Take a first and last name and format it to return the title case '''
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Result: {f_name} {l_name}"


print(format_name(input("What's your first name?"), input("What's your last name?")))
