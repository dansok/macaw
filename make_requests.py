import os.path
from typing import Dict

import requests
from requests import Response


def main():
    url: str = 'http://127.0.0.1:5000'
    headers: Dict[str, str] = {
        'Content-Type': 'application/json',
    }

    response_1: Response = requests.post(
        url=os.path.join(url, 'predict'),
        json={
            'requested': 20000,
            'annual_income': 100000,
            'apr': 2.5,
            'credit': 'good',
        },
        headers=headers,
    )
    print(f'response: {response_1.text}')

    response_2: Response = requests.get(
        url=os.path.join(url, 'get_all_models'),
        headers=headers,
    )
    print(f'response: {response_2.text}')

    response_3: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_3.text}')

    response_4: Response = requests.post(
        url=os.path.join(url, 'set_model'),
        json={
            'model_uuid': '3e8c0f9169f9400698eda70e627eba40',
        },
        headers=headers,
    )
    print(f'response: {response_4.text}')

    response_5: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_5.text}')

    response_6: Response = requests.post(
        url=os.path.join(url, 'predict'),
        json={
            'requested': 20000,
            'annual_income': 100000,
            'apr': 2.5,
            'credit': 'good',
        },
        headers=headers,
    )
    print(f'response: {response_6.text}')

    response_7: Response = requests.post(
        url=os.path.join(url, 'set_model'),
        json={
            'model_uuid': '07e219ee51554a80b721081ef777d183',
        },
        headers=headers,
    )
    print(f'response: {response_7.text}')

    response_8: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_8.text}')

    response_9: Response = requests.post(
        url=os.path.join(url, 'predict'),
        json={
            'requested': 20000,
            'annual_income': 100000,
            'apr': 2.5,
            'credit': 'good',
        },
        headers=headers,
    )
    print(f'response: {response_9.text}')


if __name__ == '__main__':
    main()
