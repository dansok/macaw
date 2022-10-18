from typing import Dict

import pandas as pd
from sklearn.linear_model import LogisticRegression

from modeling.io import IO


class Classifier:
    credit_mapping: Dict[str, int] = {
        'unknown': 0,
        'poor': 0,
        'limited': 1,
        'fair': 2,
        'good': 3,
        'excellent': 4,
    }

    @staticmethod
    def preprocess(
            leads_df: pd.DataFrame,
            offers_df: pd.DataFrame,
            clicks_df: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
        lead_offers_df: pd.DataFrame = pd.merge(
            leads_df,
            offers_df,
            how='inner',
            left_on='lead_uuid',
            right_on='lead_uuid',
        )
        data_df: pd.DataFrame = pd.merge(
            lead_offers_df,
            clicks_df,
            how='left',
            left_on='offer_id',
            right_on='offer_id',
        ).reset_index(drop=True)

        X_df: pd.DataFrame = data_df[['requested', 'annual_income', 'apr']]
        y_df: pd.DataFrame = pd.DataFrame({
            'click': ~data_df['clicked_at'].isna(),
        })

        X_df['credit'] = data_df['credit'].replace(Classifier.credit_mapping)

        return X_df, y_df

    @staticmethod
    def train(X_df: pd.DataFrame, y_df: pd.DataFrame, hyper_parameters: Dict, description: str) -> str:
        regressor: LogisticRegression = LogisticRegression(**hyper_parameters)

        # usually you would split the data into a (say, 80/20) train/test split so as to avoid overfitting
        # but since this is a toy model, and the quality of the logistic_regressor doesn't matter, we proceed "naively".

        logistic_regressor = regressor.fit(X=X_df, y=y_df.squeeze())

        return IO.write_model_artifact(model=logistic_regressor, description=description)


def main():
    # leads_df, offers_df, clicks_df = IO.read_dfs()
    # X_df, y_df = Classifier.preprocess(
    #     leads_df=leads_df,
    #     offers_df=offers_df,
    #     clicks_df=clicks_df,
    # )
    #
    # Classifier.train(
    #     X_df=X_df,
    #     y_df=y_df,
    #     hyper_parameters={
    #         'penalty': 'l2',
    #     },
    #     description='model #1',
    # )
    # Classifier.train(
    #     X_df=X_df,
    #     y_df=y_df,
    #     hyper_parameters={
    #         'solver': 'saga',
    #         'penalty': 'elasticnet',
    #         'l1_ratio': 0.5,
    #     },
    #     description='model #2',
    # )

    clf, _ = IO.read_model_artifact(model_uuid='7c023731-88ff-4167-ac19-32a76a32922b')
    df = pd.DataFrame({'requested': [20000], 'annual_income': [100000], 'apr': [2.5], 'credit': [3]})

    probability = clf.predict_proba(X=df)

    print(f'probability == {probability.squeeze()}')
    print(f'classes == {clf.classes_.tolist().index(True)}')


if __name__ == '__main__':
    main()
