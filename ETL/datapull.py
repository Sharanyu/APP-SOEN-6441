import pandas as pd
from sodapy import Socrata
import time
from configClass import config

class Extract:
    def __init__(self):
        self.configObj = config()
        self.configdf = self.configObj.readConfig()
    def get_data(self):
        # Create the client to point to the API endpoint
        data_url,app_token,data_set = self.configObj.getDataURL(self.configdf), self.configObj.getToken(self.configdf), self.configObj.getDataset(self.configdf)
        client = Socrata(data_url,app_token)
        client.timeout = 200
        start_time = time.time()
        results = client.get(data_set, limit=10000000)
        print(f"--- {time.time() - start_time} seconds ---")
        return pd.DataFrame.from_records(results)