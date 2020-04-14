import requests


def get_image(toponym_longitude, toponym_lattitude, delta='0.005'):
    try:
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        pic = requests.get(map_api_server, params=map_params)

        if pic.content:
            with open("main_image.png", 'wb') as f:
                f.write(pic.content)

            return True
        return False
    except Exception as e:
        print('error at get_image, stack:', e)
        return False