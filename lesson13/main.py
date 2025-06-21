import numpy as np
import pandas as pd

df = pd.read_csv('world.csv',index_col='國家',usecols=['國家','日期','總確診數','新增確診數','新增死亡數'])
mask = df.index == "台灣"
taiwan = df[mask]
taiwan