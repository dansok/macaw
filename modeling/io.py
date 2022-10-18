import os
import pickle
import uuid
from functools import cache
from pathlib import Path
from typing import Dict

import pandas as pd
import psycopg2
from dotenv import dotenv_values
from sklearn.linear_model import LogisticRegression
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from db.queries import (write_model_artifact_query, read_model_artifact_query, get_leads_query, get_offers_query,
                        get_clicks_query, get_all_models_query)


class IO:
    @staticmethod
    @cache
    def get_engine() -> Engine:
        project_directory: Path = Path(__file__).resolve().parent.parent
        postgres_dotenv_path: Path = Path(os.path.join(project_directory, 'docker', 'postgres', '.env'))
        postgres_env_vars: Dict[str, str] = dotenv_values(postgres_dotenv_path)
        username = postgres_env_vars['POSTGRES_USER']
        password = postgres_env_vars['POSTGRES_PASSWORD']
        database = postgres_env_vars['POSTGRES_DB']
        host = postgres_env_vars['PGHOST']
        port = postgres_env_vars['PGPORT']

        engine: Engine = create_engine(url=f'postgresql://{username}:{password}@{host}:{port}/{database}')

        return engine

    @staticmethod
    @cache
    def read_dfs() -> (pd.DataFrame, pd.DataFrame, pd.DataFrame):
        with IO.get_engine().connect() as connection:
            leads_df: pd.DataFrame = pd.read_sql(sql=get_leads_query, con=connection).fillna(value={
                'requested': 0,
                'loan_purpose': 'other',
                'credit': 'unknown',
                'annual_income': 0,
            }).reset_index(drop=True)
            offers_df: pd.DataFrame = pd.read_sql(sql=get_offers_query, con=connection).dropna(
                subset='apr').reset_index(
                drop=True)
            clicks_df: pd.DataFrame = pd.read_sql(sql=get_clicks_query, con=connection).reset_index(drop=True)

            return leads_df, offers_df, clicks_df

    @staticmethod
    def write_model_artifact(model: LogisticRegression, description: str) -> str:
        model_uuid: str = uuid.uuid4().hex

        with IO.get_engine().connect() as connection:
            pickled_model = pickle.dumps(model)

            (connection
            .execution_options(autocommit=True)
            .execute(write_model_artifact_query.format(
                model_uuid=model_uuid,
                pickled_model=psycopg2.Binary(pickled_model),
                description=description,
            )))

        return model_uuid

    @staticmethod
    def read_model_artifact(model_uuid: str) -> LogisticRegression:
        with IO.get_engine().connect() as connection:
            record = next(
                connection
                .execution_options(autocommit=True)
                .execute(read_model_artifact_query.format(model_uuid=model_uuid)))

            logistic_regression: LogisticRegression = pickle.loads(record[1])

            return logistic_regression

    @staticmethod
    def get_all_models() -> list[Dict[str, str]]:
        with IO.get_engine().connect() as connection:
            records: list = list(
                connection
                .execution_options(autocommit=True)
                .execute(get_all_models_query))

            return [{
                'model_uuid': record[0].hex,
                'description': record[1],
                'created_at': record[2].strftime('%Y-%m-%d %H:%M:%S UTC')
            } for record in records]
