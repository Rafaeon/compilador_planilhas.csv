import pandas as pd
import os


files = ["compilarplanilhas/BA.csv","compilarplanilhas/DF.csv","compilarplanilhas/FO.csv","compilarplanilhas/GO.csv","compilarplanilhas/MG.csv","compilarplanilhas/PA.csv","compilarplanilhas/PE.csv","compilarplanilhas/PO.csv","compilarplanilhas/PR.csv","compilarplanilhas/RJ.csv","compilarplanilhas/SC.csv","compilarplanilhas/SP.csv"]
#[i for i in os.listdir() if ".csv" in i]

df = pd.DataFrame()
for file in files:
    df_temp = pd.read_excel(file)
    df = pd.concat([df, df_temp])
df.to_csv("grouped7.csv", encoding="utf-8", sep=";")