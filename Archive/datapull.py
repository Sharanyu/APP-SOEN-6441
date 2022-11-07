import pandas as pd
from sodapy import Socrata
import time
import sqlite3

# configs
data_url='data.cityofnewyork.us'    
data_set='k397-673e'   
app_token='9Qn5F4x3U0TAab6TGAGQjHNCo'   
data_staging= 'C:/Users/shara/Desktop/app/NYC_payroll_data.csv'

# Create the client to point to the API endpoint
client = Socrata(data_url,app_token)
client.timeout = 200

start_time = time.time()
results = client.get(data_set, limit=10000000)
print("--- %s seconds ---" % (time.time() - start_time))

# json data converted to padnas dataframe
df = pd.DataFrame.from_records(results)

# saved as csv in local folder for cleaning purposes
df.to_csv(data_staging)