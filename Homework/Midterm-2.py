import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("test2.csv")

df["DownLink"] *= 0.06
df["UpLink"] *= 0.06

df["DownLink"] = df["DownLink"].astype(int)
df["UpLink"] = df["UpLink"].astype(int)

df["status"] = np.where(df["DownLink"] >= 15000, "High", "Low")

print(df)







