import pandas as pd
import numpy as np


typeMap={np.dtypes.Int64DType():'Integer',np.dtypes.Float64DType():'Double',np.dtypes.ObjectDType():'String'}


def join(dates={2020:[11,12],2021:[1,2]},dataDir="data/",cols=list(range(56))):
    dfs=[]
    for year in dates:
        for month in dates[year]:
            fileName=f"On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_{year}_{month}.csv"
            df=pd.read_csv(dataDir+fileName,low_memory=False)
            columns=df.columns[cols]
            newColumns=[columns[i]+f"({typeMap[t]})" for i,t in enumerate(df.dtypes.iloc[cols]) ]
            df=df[columns]
            df.rename(columns=dict(zip(columns, newColumns)),inplace=True)
            dfs.append(df)
    df=pd.concat(dfs,ignore_index=True)
    df.to_csv("flights.csv",index=False)
    
