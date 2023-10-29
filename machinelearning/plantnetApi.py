# coding=utf-8

import requests
import json
from pprint import pprint


def plant_detect(img_path):
    API_KEY = "2b10US62U13eKlePzvEr3au"	# Your API_KEY here
    PROJECT = "all"; # try specific floras: "weurope", "canada"…
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    print(img_path)

    image_path_1  = img_path
    # image_path_1 = "D:/Python/plant_disease/crop-pest-control-system-based-on-image-recognition-develop/daoctor/机器学习/test_/False smut -1.jpg"
    # image_path_1 = "D:/Python/plant_disease/crop-pest-control-system-based-on-image-recognition-develop/daoctor/机器学习/test_/image.jpg"
    image_data_1 = open(image_path_1, 'rb')

    # image_path_2 = "D:/Python/plant_disease/crop-pest-control-system-based-on-image-recognition-develop/daoctor/机器学习/test_/desk_2.jpg"
    # image_data_2 = open(image_path_2, 'rb')

    # data = {
    # 'organs': ['flower', 'leaf']
    # }

    data = {
    'organs': ['leaf']
    }

    files = [
    ('images', (image_path_1, image_data_1)),
    # ('images', (image_path_2, image_data_2))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    # print(response.status_code) 

    if response.status_code == 200:
        json_result = json.loads(response.text)
        # pprint(json_result)
        best_match = json_result['bestMatch']
        scientific_name = json_result['results'][0]['species']['scientificNameWithoutAuthor']
    else:
        best_match = ""
        scientific_name = ""

    pprint(best_match)
    pprint(scientific_name)

    return response.status_code, best_match, scientific_name
			