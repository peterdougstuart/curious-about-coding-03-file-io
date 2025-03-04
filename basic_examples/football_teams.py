print("Using a list")

list_of_favourite_teams = ["Spurs", "Liverpool", "Chelsea", "Watford", "Villa"]

list_of_favourite_teams.append("Arsenal")

print("First team in list", list_of_favourite_teams[0])

for item in list_of_favourite_teams:
    print("- ", item)

print("Using a dictionary")

dictionary_of_favourite_teams_by_person = {
    "Louis": "Spurs",
    "Leticia": "Liverpool",
    "Abdi": "Chelsea",
    "Gaurav": "Watford",
    "Peter": "Villa",
}

print("Louis's favourite team is", dictionary_of_favourite_teams_by_person["Louis"])

dictionary_of_favourite_teams_by_person["Louis"] = "Arsenal"

print("Louis's favourite team is", dictionary_of_favourite_teams_by_person["Louis"])

# print("Stephen's favourite team is", dictionary_of_favourite_teams_by_person["Stephen"])

dictionary_of_favourite_teams_by_person["Stephen"] = "Arsenal"

print("Stephen's favourite team is", dictionary_of_favourite_teams_by_person["Stephen"])


dictionary_of_favourite_teams_by_person_by_country = {
    "Abdi": {
        "England": "Chelsea",
        "Spain": "Barcelona",
    },
    "Peter": {
        "England": "Villa",
        "Spain": "Real Madrid",
    },
}


print(dictionary_of_favourite_teams_by_person_by_country["Abdi"]["Spain"])

# Looping over a dictionary

for x in dictionary_of_favourite_teams_by_person:
    print(x, ":", dictionary_of_favourite_teams_by_person[x])

for key, value in dictionary_of_favourite_teams_by_person.items():
    print(key, ":", value)

for value in dictionary_of_favourite_teams_by_person.values():
    print(value)

#  checking if a key exists in a dictionary

if "Louis" in dictionary_of_favourite_teams_by_person:
    print(dictionary_of_favourite_teams_by_person["Louis"])
else:
    print("No favourite team")

# getting a value from a dictionary with a default value

print(dictionary_of_favourite_teams_by_person.get("Sam", "No favourite team"))
