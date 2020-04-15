from pprint import pprint

import requests


def get_cords(toponym_to_find, apikey='40d1649f-0493-4b70-98ba-98533de7710b', format='json' ):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": apikey,
        "geocode": toponym_to_find,
        "format": format}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    # print(response)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    metadata = toponym['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    return toponym_coodrinates.split(), metadata
