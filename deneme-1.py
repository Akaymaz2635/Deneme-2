import pandas as pd

veri=pd.read_csv("C:/Users/alika/Desktop/Reporter_Project/Inputs/1.csv")

print(veri[['Check']].to_string(index=False))