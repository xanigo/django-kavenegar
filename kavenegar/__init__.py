import json

import requests
from django.conf import settings

__version__ = '0.1.0.dev'

API_KEY = settings.ZARINPAL['API_KEY']


def send_otp(receptor: int, template: str, token: str, token2: str = None, token3: str = None):
    resp = requests.post(
        url=f'https://api.kavenegar.com/v1/{API_KEY}/verify/lookup.json',
        data={
            'receptor': receptor,
            'template': template,
            'token': token,
            'token2': token2,
            'token3': token3,
            'type': 'sms',
        },
    )

    return json.loads(resp.content.decode('utf-8'))
