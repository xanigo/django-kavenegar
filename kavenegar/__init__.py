import json

import requests
from django.conf import settings

__version__ = '0.1.0.dev'

API_KEY = settings.KAVENEGAR['API_KEY']
TEMPLATE = settings.KAVENEGAR.get('TEMPLATE')


def send_otp(receptor: int, token: str, token2: str = None, token3: str = None, template: str = None) -> dict:
    resp = requests.post(
        url=f'https://api.kavenegar.com/v1/{API_KEY}/verify/lookup.json',
        data={
            'receptor': receptor,
            'template': template or TEMPLATE,
            'token': token,
            'token2': token2,
            'token3': token3,
            'type': 'sms',
        },
    )

    return json.loads(resp.content.decode('utf-8'))
