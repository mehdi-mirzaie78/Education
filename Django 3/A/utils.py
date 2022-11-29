def send_otp_code(phone_number, code):
    pass


# TODO: Can you make it async?
"""
from kavenegar import *

def send_otp_code(phone_number, code):
    API_KEY = ''
    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
"""
