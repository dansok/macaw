from modeling.classifier import Classifier
from modeling.io import IO


def main():
    leads_df, offers_df, clicks_df = IO.read_dfs()
    X_df, y_df = Classifier.preprocess(
        leads_df=leads_df,
        offers_df=offers_df,
        clicks_df=clicks_df,
    )

    Classifier.train(
        X_df=X_df,
        y_df=y_df,
        hyper_parameters={
            'penalty': 'l2',
        },
        description='model #1',
    )
    Classifier.train(
        X_df=X_df,
        y_df=y_df,
        hyper_parameters={
            'solver': 'saga',
            'penalty': 'elasticnet',
            'l1_ratio': 0.5,
        },
        description='model #2',
    )


if __name__ == '__main__':
    main()
