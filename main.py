import requests
import csv

url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
file_path = "pokemons.csv"

response_geral_list = requests.get(url)
poke_list = response_geral_list.json()
poke_end_points = []

for item in poke_list["results"]:
    poke_end_points.append(item['url'])

poke_dict = {}
for poke in poke_end_points:
    poke_especify = requests.get(poke)
    poke_especify_list = poke_especify.json()
    poke_dict[poke_especify_list['name']] = {
        "id": poke_especify_list['id'],
        "base_experience": poke_especify_list['base_experience'],
        "height": poke_especify_list['height'],
        "weight": poke_especify_list['weight']
    }
headers = ['name', 'id', 'base_experience', 'height', 'weight']

with open(file_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerow(headers)
    for name, stats in poke_dict.items():
        row = [name, stats['id'], stats['base_experience'], stats['height'], stats['weight']]
        writer.writerow(row)
