# Send stream Carriots using a Python library

Class to send stream to Carriots for IoT projects using a Python library

## Edit values to Config file

    # Config.py
    carriots_config = dict(
        api_url="http://api.carriots.com",
        api_account="Your username at login",
        api_key_stream="Api Key for send stream",
        api_key_full="Full privileges. EDIT ONLY IF IS NECESSARY"
    )

## Example:

    from Carriots import Carriots
    carriots = Carriots()

### Example: Send stream:
    # device: Device name registered at Carriots platform
    device = "device1"

    # data: Dictionary with the values of the sensors
    data = {
        'sensor1': 'value1',
        'sensor2': 'value2'
    }

    carriots.send_stream(device, data)

Response:
    `HTTP_response, content`
### Example: Get device info
    # device: Device name registered at Carriots platform
    device = "device1"

    carriots.get_device_info(device)
Response:
    `HTTP_response, content`