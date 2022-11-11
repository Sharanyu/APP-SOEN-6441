import pandas as pd
from sodapy import Socrata
import time
from configClass import Config

class Extract:
    def __init__(self):
        self.configObj = Config()
        self.configdf = self.configObj.read_config()
    def get_data(self):
        # Create the client to point to the API endpoint
        data_url,app_token,data_set = self.configObj.get_data_url(self.configdf), self.configObj.get_token(self.configdf), self.configObj.get_dataset(self.configdf)
        client = Socrata(data_url,app_token)
        client.timeout = 200
        start_time = time.time()
        results = client.get(data_set, limit=100000)
        print(f"--- {time.time() - start_time} seconds ---")
        return pd.DataFrame.from_records(results)