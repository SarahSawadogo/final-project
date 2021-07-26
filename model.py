import requests
# # import random
# # response = requests.get(giphy_request_link.json())
def worldList(country):
    response = requests.get('https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json').json()
    return response["countries"][country]
#iterate through the list until the value for name in the dictionary matches the user search
    # for entry in response:
    #     if entry['afghanistan'] == country:
    #         return entry
(worldList('japan'))
# # for entry in range(3):
# #     print(response[random.randint(0, 100)]["images"]["fixed_height"]["url"])
