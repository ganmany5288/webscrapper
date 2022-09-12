import pandas as pd
import numpy as np

df = pd.read_csv("gpu_recordsFORREAL.csv")

gpu_list = ["3060", "3060 Ti", "3070", "3070 Ti", "3080", "3080 Ti", "3090", "3090 Ti","6700", "6700 XT", "6800", "6800 XT", "6900 XT", "6950 XT"]


flag = True

while flag:
    gpu_name = input("What GPU would you like to see: ")
    if gpu_name not in gpu_list:
        print("Please enter a valid name")
    else:
        gpu = df[(df['Title'] == gpu_name)]
        gpu.sort_values("Price", inplace = True)
        flag = False

print("Here ya go!\n")
print(gpu)

print('\n')

bool_series = gpu["Brand"].duplicated(keep = False)

print(bool_series)


gpu = gpu[~bool_series]
print(gpu.info())
print(gpu)