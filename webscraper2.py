import pandas as pd
import numpy as np

data = pd.read_csv("gpu_recordsFORREAL.csv")

data.columns = [column.replace(" ", "_") for column in data.columns]

data.query(Brand == MSI)


print(data)