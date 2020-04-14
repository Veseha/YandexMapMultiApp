import requests


def get_image(toponym_longitude, toponym_lattitude, delta='0.005', zoom=10):
    try:
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "l": "map"
        }
        if zoom:
            map_params["zoom"] = zoom
        else:
            map_params["spn"] = ",".join([delta, delta])
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