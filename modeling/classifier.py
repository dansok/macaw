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
