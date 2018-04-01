# -*-coding:utf8-*-

__author__ = "Indestim Technologies SLU"
__credits__ = "Christian Escalante"
__email__ = "cescalante@indestim.es"
__created__ = "01 Apr 2018"

import json
import requests
from Config import carriots_config


class Carriots (object):
    __api_url = carriots_config['api_url']

    def __init__(self, client_type='json'):
        self.__client_type = client_type
        self.__api_key = carriots_config['api_key_stream']
        self.__content_type = "application/vnd.carriots.api.v2+%s" % self.__client_type
        self.__headers = {
            'Content-Type': self.__content_type,
            'Accept': self.__content_type,
            'Carriots.apikey': self.__api_key
        }

    def send_stream(self, device_name, data):
        """
        Method to send 'stream' to Carriots API
        :param device: Device registered
        :param data: Dictionary of data included in the stream
        :return: HTTP, content  Ex.: 200, {'response': 'OK'}
        """

        url = '{api_url}/streams'.format(api_url=self.__api_url)

        payload = {
            "protocol": "v2",
            "device": self.__normalize_device(device_name),
            "at": "now",
            "data": data
        }

        response = requests.post(url, json=payload, headers=self.__headers)

        return response.status_code, to_json(response.content)

    def get_device_info(self, device_name):
        api_key_current = self.__headers['Carriots.apikey']
        self.__headers['Carriots.apikey'] = carriots_config['api_key_full']

        url = '{api_url}/devices/{device}'.format(api_url=self.__api_url, device=self.__normalize_device(device_name))
        response = requests.get(url, headers=self.__headers)

        self.__headers['Carriots.apikey'] = api_key_current
        return response.status_code, to_json(response.content)

    def __normalize_device(self, device_name):
        return device_name + "@{account}.{account}".format(account=carriots_config['api_account'])


def to_json(req):
    """
    Convert bytes to JSON: response.content
    :param req: response
    :return: json
    """
    content = req.decode('utf8')
    return json.loads(content)
