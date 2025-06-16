import pandas as pd
import vnquant.data as dt

try: 
        
    stock_codes = ["SHB", "FCN", "VPB", "HDB", "MBB", "CTG", "VIB", "TPB", "MSB", "ACB"]

    for code in stock_codes:
        
        loader = dt.DataLoader(
            [code],
            "2005-01-01",
            pd.to_datetime('today').strftime('%Y-%m-%d'),
            data_source="CAFE",
            minimal=True,
            table_style="prefix",
        )
        data = loader.download()

        data.to_csv('data/stock_data_'+code+'.csv', header=True, index=True)
        
        print ("Get Stock data of " + code + " done")
except: 
    print("An exception occurred")


