print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
min_height_in_cm = 120

if height >= min_height_in_cm:
    print("Your can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want photo taken? Y or N ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
