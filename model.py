import requests
# # import random
# # response = requests.get(giphy_request_link.json())
def worldList(country):
    response = requests.get('https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json').json()
    return response["countries"][country]
def city(country_img):
    response = requests.get('https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json').json()
    return response[country_img]
# def worldImageList(country):
#     response = requests.get('https://restcountries.eu/rest/v2/all').json()
#     return response["countries"][country]
#iterate through the list until the value for name in the dictionary matches the user search
    # for entry in response:
    #     if entry['afghanistan'] == country:
    #         return entry
(worldList('japan'))
# # for entry in range(3):
# #     print(response[random.randint(0, 100)]["images"]["fixed_height"]["url"])
#iterate through the list until the value for name in the dictionary matches the user search
    # for entry in response:
    #     if entry['afghanistan'] == country:
    #         return entry
(worldList('japan'))
# # for entry in range(3):
# #     print(response[random.randint(0, 100)]["images"]["fixed_height"]["url"])
home_country= {
    "canada":"https://museum-id.com/wp-content/uploads/2018/06/ROM.jpg",
    "mexico":"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQFqhDwrWGBA-l4IqAVKJd7YkXRQjw6YAPA2fN-ZbYMtB_klYIWY3SjqwFYo7LL-qypG3EvfJydXyRSkmsDxebFSg",
    "nicaragua":"https://s.abcnews.com/images/GMA/volcano-main-ss-ps-200228_hpMain_16x9_608.jpg",
    "argentina":"https://www.planetware.com/photos-large/ARG/argentina-top-attractions-patagonia.jpg",
    "uruguay":"http://theatreprojects.com/files/layout/contact-santiago-chile.jpg",
    "chile":"https://i3.visitchile.com/img/GalleryContent/4431/slider/Laguna_San_Rafael.jpg",
    "south africa":"https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzL2Q0NzRiZTg4NWM5NGQyYTg2NV8xNDIwMTM2MTQ1NV8wN2YzMWEyM2VhX28tbGFuY3pvczMuanBnIl0sWyJwIiwiY29udmVydCIsIiJdLFsicCIsImNvbnZlcnQiLCItcXVhbGl0eSA4MSAtYXV0by1vcmllbnQiXSxbInAiLCJ0aHVtYiIsIjYwMHg-Il1d/14201361455_07f31a23ea_o-lanczos3.jpg",
    "morocco":"https://cdn.theculturetrip.com/wp-content/uploads/2016/11/shutterstock_251302651.jpg",
    "somalia":"https://cdn.thecrazytourist.com/wp-content/uploads/2017/01/Hargeisa.jpghttps://cdn.thecrazytourist.com/wp-content/uploads/2017/01/Hargeisa.jpg",
    "cambodia":"https://www.planetware.com/photos-large/CAM/cambodia-angkor-wat.jpg",
    "saudi arabia":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStPGCJn4AlJDjF6rKnKllKCcEOUAIWCu_FeHPxkWjEuvQnYIbEW39QUTG-h0D6Xu7paTIMOG8t2l7tTJ-KjaSh3A",
    "phillipines":"https://i0.wp.com/unusualplaces.org/wp-content/uploads/2019/05/chocolatehills.jpg",
    "australia":"https://www.planetware.com/photos-large/AUS/australia-new-south-wales-sydney-harbour-bridge.jpg",
    "fiji":"https://www.planetware.com/photos-large/FJ/fiji-pacific-harbour.jpg",
    "new zealand":"https://www.planetware.com/photos-large/NZ/new-zealand-south-island-fiordland-national-park.jpg",
    "netherlands":"https://www.planetware.com/photos-large/NL/netherlands-amsterdam-jordaan-canal.jpg",
    "switzerland":"https://gate1connections.files.wordpress.com/2018/09/chapelbridge_lucerne.jpg",
    "ukraine":"https://www.planetware.com/wpimages/2019/11/ukraine-top-attractions-odessa-opera-ballet.jpg"
}