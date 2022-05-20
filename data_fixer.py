import pandas as pd

def fix(coordinate_string):
    new_str = coordinate_string.replace(',','.')
    new_str = new_str.replace('.','')
    new_str = "".join([x for x in new_str if x.isnumeric()])
    coordinate = new_str[:2] + '.' + new_str[2:]
    return coordinate

df = pd.read_csv("2021-yl-istanbulkart-dolum-merkezi-bilgileri.csv", sep=";")
df["LATITUDE"] = df["LATITUDE"].apply(fix)
df["LONGITUDE"] = df["LONGITUDE"].apply(fix)
df["COUNTY_NAME"] = df["COUNTY_NAME"].apply(str.strip).apply(str.capitalize)
df.to_csv("data.csv",sep=";",index=False)