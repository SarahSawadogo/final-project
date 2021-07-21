import requests
# import random
# response = requests.get(giphy_request_link.json())

def getImageUrlFrom(query):
    giphy_request_link = "https://api.giphy.com/v1/gifs/search?api_key=CTUfMZQ5zxf8SMRLRW02UkpfVhn7FJL4&q=dog&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(giphy_request_link).json()
    return response ["data"][0]["images"]["fixed_height"]["url"]

# for entry in range(3):
#     print(response[random.randint(0, 100)]["images"]["fixed_height"]["url"])