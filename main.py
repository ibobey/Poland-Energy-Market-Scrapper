import requests
import pandas as pd

RAW_URL = "https://www.pse.pl/getcsv/-/export/csv/EN_CENY_NIEZB_RB/data/20230709"

response = requests.get(url=RAW_URL)

data = response.content

data = data.decode('ascii')
df = pd.DataFrame([x.split(';') for x in data.split('\n')])
print(df)


