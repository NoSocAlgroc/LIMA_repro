import requests
import zipfile
import io
import os



def fetch(years=list(range(2020,2025)),months=list(range(1,13)),dataDir="data/",cols=list(range(56))):
    os.makedirs(dataDir, exist_ok=True)
    for year in years:
        for month in months:
            fileName=f"On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"
            url="https://transtats.bts.gov/PREZIP/"+fileName
            response = requests.get(url, stream=True)
            response.raise_for_status()  # stop if error

            if os.path.exists(dataDir+fileName):
                continue
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                print(f"Extracting {url} -> {dataDir}")
                z.extractall(dataDir)