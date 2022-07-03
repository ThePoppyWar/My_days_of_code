student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     {"country": "German", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visit_time, cities: list):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit_time
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

