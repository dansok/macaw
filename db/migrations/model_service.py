import os
from pathlib import Path

import pandas as pd
from sqlalchemy.engine import Engine

from db.queries import truncation_query
from utils.sql_utils import get_engine


def main():
    project_directory: Path = Path(__file__).resolve().parent.parent.parent
    data_path: Path = Path(os.path.join(project_directory, 'data'))

    df_leads = pd.read_parquet(os.path.join(data_path, 'ds_leads.parquet.gzip'))
    df_offers = pd.read_parquet(os.path.join(data_path, 'ds_offers.parquet.gzip'))
    df_clicks = pd.read_parquet(os.path.join(data_path, 'ds_clicks.parquet.gzip'))

    engine: Engine = get_engine()

    with engine.connect() as connection:
        (connection
         .execution_options(autocommit=True)
         .execute(truncation_query))

        df_leads.to_sql(name='leads', con=connection, index=False, if_exists='append')
        df_offers.to_sql(name='offers', con=connection, index=False, if_exists='append')
        df_clicks.to_sql(name='clicks', con=connection, index=False, if_exists='append')


if __name__ == '__main__':
    main()
