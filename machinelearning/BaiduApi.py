# coding=utf-8

import json
import base64
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'HnAbTTBA20TEkGDT21URtN81'

SECRET_KEY = 'YXiKdXWOm35ZY8Pum4y5i7ERs1d2aznD'


IMAGE_RECOGNIZE_URL = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()

"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

"""
    调用菜品识别接口并打印结果
"""
def print_result(filename, url):
    # 获取图片
    file_content = read_file(filename)

    response = request(url, urlencode(
        {
            'image': base64.b64encode(file_content),
            'top_num': 1
        }))
    result_json = json.loads(response)

    # 打印图片结果
    print(result_json)
    # for data in result_json["result"]:
    #     print(u"  菜品名称: " + data["name"])
    #     if data[u'has_calorie']:
    #         print(u"  菜品热量: " + data["calorie"])

def GetResult(file):
    # 获取access token
    token = fetch_token()

    # 拼接图像识别url
    url = IMAGE_RECOGNIZE_URL + "?access_token=" + token

    response = request(url, urlencode(
        {
            'image': base64.b64encode(file),
            'top_num': 1
        }))
    result_json = json.loads(response)
    return result_json

if __name__ == '__main__':
    url=""
    print("菜品1")
    print_result("./upload/food.jpeg", url)
