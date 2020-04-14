import requests


def get_image(toponym_longitude, toponym_lattitude, delta='0.005', zoom=10):
    toponym_lattitude = str(toponym_lattitude)
    toponym_longitude = str(toponym_longitude)
    try:

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "l": "map"
        }
        if zoom != -1:
            map_params["z"] = zoom
        else:
            map_params["spn"] = ",".join([delta, delta])
        print('map_params are', map_params)
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        pic = requests.get(map_api_server, params=map_params)
        print(pic.url)

        if pic.content:
            with open("main_image.png", 'wb') as f:
                f.write(pic.content)

            return True
        return False
    except Exception as e:
        print('error at get_image, stack:', e)
        return False