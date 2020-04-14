import requests
from PIL import Image


def get_image(toponym_longitude, toponym_lattitude, delta='0.005', zoom=10, l='sat'):
    toponym_lattitude = str(toponym_lattitude)
    toponym_longitude = str(toponym_longitude)
    try:

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "l": l
        }
        if zoom != -1:
            map_params["z"] = zoom
        else:
            map_params["spn"] = ",".join([delta, delta])
        # -------------------------------------------------------- print('map_params are', map_params)
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        pic = requests.get(map_api_server, params=map_params)
        # ---------------------------------------------------print(pic.url)

        if pic.content and l != 'sat':
            with open("main_image.png", 'wb') as f:
                f.write(pic.content)
        elif pic.content:
            # ----------------------------------------print('select jpg format')
            with open("main_image.jpg", 'wb') as f:
                f.write(pic.content)
            im1 = Image.open(r'main_image.jpg')
            im1.save(r'main_image.png')

            return True
        return False
    except Exception as e:
        print('error at get_image, stack:', e)
        return False