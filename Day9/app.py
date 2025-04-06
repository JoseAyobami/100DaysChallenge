# An empty dictionay
# student = {}

# assigning data to a dictionary
# student["name"] = "Ayobami"
# print(student)

# changing the value of an existing key
# student["name"] = "Landon"
# print(student)

# Loop in dictionary
student = {
    "name": "Jose",
    "age": 26,
    "dream_job": "Backend developer",
    "nationality": "Nigeria"
}

# for key in student:
#     print(key)

# for value in student:
#     print(student[value])

# travel_log = {
#     "France": ["Paris", "Lillie", "Dijon"],
#     "Germany": ["Berlin", "Valencia"]
# }


# print(travel_log["France"])

travel_log = {
    "France": {
        "cities_visited" : ["Paris", "Lillie", "Dijon"],
        "total_visits" : 8 
    },
    "Germany": {
        "cities_visited": ["Berlin", "Bvb", "Nice"],
        "total_visited": 12
    }
}

print(travel_log["Germany"]["cities_visited"][0])

# print(travel_log["France"])