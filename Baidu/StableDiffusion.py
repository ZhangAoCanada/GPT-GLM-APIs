import requests
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv
import base64
import cv2
import numpy as np

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}"
    url = url.format(API_Key=os.getenv('API_Key'), Secret_Key=os.getenv('Secret_Key'))
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/text2image/sd_xl?access_token=" + get_access_token()
    
    payload = json.dumps({
        "prompt": "cat",
        "negative_prompt": "white",
        "size": "1024x1024",
        "steps": 20, 
        "n": 2,
        "sampler_index": "DPM++ SDE Karras" 
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

    ### NOTE: decode all images ### 
    for image_response in response.json()['data']:
        if image_response['object'] == "image":
            image_base64 = image_response['b64_image']
            image_data = base64.b64decode(image_base64)
            image_array = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            index = image_response['index']
            cv2.imwrite("./response_{index}.jpg".format(index=index), image)

if __name__ == '__main__':
    main()