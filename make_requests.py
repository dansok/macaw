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
    print(f'response: {response_1.json()}')

    response_2: Response = requests.get(
        url=os.path.join(url, 'get_all_models'),
        headers=headers,
    )
    print(f'response: {response_2.json()}')

    response_3: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_3.json()}')

    response_4: Response = requests.post(
        url=os.path.join(url, 'set_model'),
        json={
            'model_uuid': 'b31d8dfd67b14c05b7aca5c2fe8d7c95',
        },
        headers=headers,
    )
    print(f'response: {response_4.json()}')

    response_5: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_5.json()}')

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
    print(f'response: {response_6.json()}')

    response_7: Response = requests.post(
        url=os.path.join(url, 'set_model'),
        json={
            'model_uuid': '57ea52a4bd684e83987573f903805556',
        },
        headers=headers,
    )
    print(f'response: {response_7.json()}')

    response_8: Response = requests.get(
        url=os.path.join(url, 'get_current_model'),
        headers=headers,
    )
    print(f'response: {response_8.json()}')

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
    print(f'response: {response_9.json()}')


if __name__ == '__main__':
    main()
