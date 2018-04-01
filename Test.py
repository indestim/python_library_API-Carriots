# -*-coding:utf8-*-

__author__ = "Indestim Technologies SLU"
__credits__ = "Christian Escalante"
__email__ = "cescalante@indestim.es"
__created__ = "01 Apr 2018"

import status

from Carriots import Carriots
from requests.exceptions import ConnectionError, RequestException

carriots = Carriots()

# ===============
# Ex. Send Stream
# ================

device = "device1"
data = {
    'sensor1': 'value1',
    'sendor2': 'value2'
}

try:
    http_response, content = carriots.send_stream(device, data)

    if http_response == status.HTTP_200_OK:
        print("Send stream: OK")
    elif http_response == status.HTTP_401_UNAUTHORIZED:
        print("Response: {response}".format(response=content['response']))
    elif http_response == status.HTTP_500_INTERNAL_SERVER_ERROR:
        print("Internal Server Error.")
    else:
        print("Other. HTTP response: {http}".format(http=http_response))
except ConnectionError as ex:
    print("Connection Error: {ex}".format(ex=ex))
    exit(0)
except RequestException as e:
    print("Request exception: {e}".format(e=e))
    exit(1)


# ===================
# Ex. Get device info
# ===================

device = "device2"

try:
    http_response, content = carriots.get_device_info(device)

    if http_response == status.HTTP_200_OK:
        print("'owner': {owner}".format(owner=content['owner']))
        print("'id_developer': {developer}".format(developer=content['id_developer']))
        print("'time_zone': {time_zone}".format(time_zone=content['time_zone']))
    elif http_response == status.HTTP_401_UNAUTHORIZED:
        print("Response: {response}".format(response=content['message']))
    elif http_response == status.HTTP_500_INTERNAL_SERVER_ERROR:
        print("Internal Server Error.")
    else:
        print("Other. HTTP response: {http}".format(http=http_response))
except ConnectionError as ex:
    print("Connection Error: {ex}".format(ex=ex))
    exit(0)
except RequestException as e:
    print("Request exception: {e}".format(e=e))
    exit(1)
