import requests
# create response  variable and send get to rick and morty api using requests library
response = requests.get("https://rickandmortyapi.com/api/character")
# verify response status is 200 which means successful
assert response.status_code == 200


print(data['info']['count'])
assert data['info']['count'] == 671

print(data['results'][0]['name'])