import pandas as pd


class Config:
    def __init__(self):
        pass

    def read_config(self):
        return pd.read_csv("configs.csv", quotechar="'")

    def get_staging(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "staginglocation"'
        ).value.values.tolist()[0]

    def get_data_url(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "data_url"'
        ).value.values.tolist()[0]

    def get_dataset(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "data_set"'
        ).value.values.tolist()[0]

    def get_database(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "database"'
        ).value.values.tolist()[0]

    def get_token(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "app_token"'
        ).value.values.tolist()[0]
