import pandas as pd
import os 

os.chdir('task1') # почему-то скрипт запускается из корневой папки

print(os.getcwd())

full_path_csv, n_row, n_col = input().split()

df = pd.read_csv(full_path_csv, delimiter=',', header=None)

print(df.iloc[int(n_row), int(n_col)])