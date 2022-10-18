```python3
import requests

requests.post(
    url='http://127.0.0.1:5000/predict',
    json={
        'requested': 20000,
        'annual_income': 100000,
        'apr': 2.5,
        'credit': 'good',
    },
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'click_probability': 0.0009745618015403553}

requests.get(
    url='http:127.0.0.1:5000/get_all_models',
    headers={
        'Content-Type': 'application/json',
    },
)
response: [{'created_at': '2022-10-18 19:39:10 UTC', 'description': 'model #1', 'model_uuid': 'b31d8dfd67b14c05b7aca5c2fe8d7c95'}, {'created_at': '2022-10-18 19:39:16 UTC', 'description': 'model #2', 'model_uuid': '57ea52a4bd684e83987573f903805556'}]

requests.get(
    url='http://127.0.0.1:5000/get_current_model',
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'model_uuid': '57ea52a4bd684e83987573f903805556'}

requests.post(
    url='http://127.0.0.1:5000/set_model',
    json={
        'model_uuid': 'b31d8dfd67b14c05b7aca5c2fe8d7c95',
    },
    headers={
        'Content-Type': 'application/json',
    },
)
response: {}

requests.get(
    url='http://127.0.0.1:5000/get_current_model',
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'model_uuid': 'b31d8dfd67b14c05b7aca5c2fe8d7c95'}

requests.post(
    url='http://127.0.0.1:5000/predict',
    json={
        'requested': 20000,
        'annual_income': 100000,
        'apr': 2.5,
        'credit': 'good',
    },
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'click_probability': 0.026067497479385218}

requests.post(
    url='http://127.0.0.1:5000/set_model',
    json={
        'model_uuid': '57ea52a4bd684e83987573f903805556',
    },
    headers={
        'Content-Type': 'application/json',
    },
)
response: {}

requests.get(
    url='http://127.0.0.1:5000/get_current_model',
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'model_uuid': '57ea52a4bd684e83987573f903805556'}

requests.post(
    url='http://127.0.0.1:5000/predict',
    json={
        'requested': 20000,
        'annual_income': 100000,
        'apr': 2.5,
        'credit': 'good',
    },
    headers={
        'Content-Type': 'application/json',
    },
)
response: {'click_probability': 0.0009745618015403553}
```
