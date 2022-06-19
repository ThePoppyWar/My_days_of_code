print("Welcome to the band generator")
city = input("Which city did you grew uo in?\n")
pet = input("What is the name of a pet?\n")
print(f"Your band name could be {city} {pet}")

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $ "))
people = int(input("How many people to split the bill? "))
proc = int(input("How procentage tip would you like to give? 10, 12 or 15 "))
print(f"Each person should pay: % {round(((total_bill + (total_bill * proc / 100))/people), 1)}")

age = input("What is your current age? ")
age = int(age)
years_remaining = 90 - age
days_of_year = 365 * years_remaining
weeks_of_year = 52 * years_remaining
months_of_year = 12 * years_remaining

print(f"You have {days_of_year} days, {weeks_of_year}, and {months_of_year} months left")

