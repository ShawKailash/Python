import requests
req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(person)
print(f"name is\t\t{person['name']}")
print(f"birth year is\t\t{person['birth_year']}")

print("film involved in:")
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("film is: ",film['title'])
