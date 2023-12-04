import requests
import json

ship_url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
response = requests.get(ship_url)
data = response.json()

ship_details_url = data['results'][0]['url']
ship_response = requests.get(ship_details_url)
ship_data = ship_response.json()

pilots_info = []
for pilot_url in ship_data["pilots"]:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    homeworld_url = pilot_data["homeworld"]

    homeworld_response = requests.get(homeworld_url)
    homeworld_data = homeworld_response.json()

    pilot_info = {
        "height": pilot_data["height"],
        "homeworld": homeworld_data["name"],
        "homeworld_url": pilot_data["homeworld"],
        "mass": pilot_data["mass"],
        "name": pilot_data["name"],
    }
    pilots_info.append(pilot_info)

info = {
    "ship_name": ship_data["name"],
    "starship_class": ship_data["starship_class"],
    "max_atmosphering_speed": ship_data["max_atmosphering_speed"],
    "pilots": pilots_info
}

print(json.dumps(info, indent=4))

with open("info.json", "w") as file:
    json.dump(info, file, indent=4)