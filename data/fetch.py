import requests
import zipfile
import io
import os



def fetch(dates={2020:[11,12],2021:[1,2]},dataDir="data/",cols=list(range(56))):
    os.makedirs(dataDir, exist_ok=True)
    for year in dates:
        for month in dates[year]:
            
            fileName=f"On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"
            csvName=f"On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_{year}_{month}.csv"
            if os.path.exists(dataDir+csvName):
                continue
            url="https://transtats.bts.gov/PREZIP/"+fileName
            response = requests.get(url, stream=True)
            response.raise_for_status()  # stop if error

            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                print(f"Extracting {url} -> {dataDir}")
                z.extractall(dataDir)