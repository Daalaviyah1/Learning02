people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Revenclew"},
    {"name": "Draco", "house": "SLytherin"}
]
# def f(person):
#     return person["name"] # Or sort by "house".

# people.sort(key=f)

#Or we can use Lamda function
people.sort(key=lambda person: person["name"])

print(people)