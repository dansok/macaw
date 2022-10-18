from http.client import CONFLICT, INTERNAL_SERVER_ERROR, OK

import pandas as pd
from flask import Flask, request, Response

from model_service.state import State
from modeling.classifier import Classifier
from modeling.io import IO

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if State.model_uuid is None:
        return Response(response='Must set application\'s model before attempting prediction\n', status=CONFLICT)

    request_data = request.get_json()
    print(f'request_data == {request_data}')

    try:
        requested: int = int(request_data.get('requested'))
        annual_income: int = int(request_data.get('annual_income'))
        apr: int = int(request_data.get('apr'))
        credit: int = Classifier.credit_mapping[request_data.get('credit')]

        logistic_regressor, _ = IO.read_model_artifact(model_uuid=State.model_uuid)

        probabilities: list[float] = logistic_regressor.predict_proba(X=pd.DataFrame({
            'requested': [requested],
            'annual_income': [annual_income],
            'apr': [apr],
            'credit': [credit],
        })).squeeze().tolist()

        click_probability: float = probabilities[logistic_regressor.classes_.tolist().index(True)]

        return {'click_probability': click_probability}, OK
    except Exception as exception:
        print(exception)
        return Response(
            response='An internal error occurred. Check your request body contains all 4 necessary parameters.\n',
            status=INTERNAL_SERVER_ERROR)


@app.route('/set_model', methods=['POST'])
def set_model():
    try:
        model_uuid: str = request.get_json().get('model_uuid')
        State.model_uuid = model_uuid

        return {}, OK
    except Exception as exception:
        print(exception)
        return Response(
            response='An internal error occurred. Make sure to pass a proper model uuid.\n',
            status=INTERNAL_SERVER_ERROR)


@app.route('/get_model', methods=['GET'])
def get_model():
    return {'model_uuid': State.model_uuid}, OK


if __name__ == '__main__':
    app.run()
