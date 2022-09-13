import requests

name = input("Enter your Pokemon name: ")
name = name.lower()
link = f"https://pokeapi.co/api/v2/pokemon/{name}"

req = requests.get(link)

if req.status_code == 200:
    pokemon = req.json()

    for index in pokemon['game_indices']:
        print(index)

else:
    print("Something went Wrong! Record Not found")