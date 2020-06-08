"""
Created on TUE JUN 9 00:01:00 2020

@description Calculate Internal Rate of Return(IRR)
@author Richard
"""

#%%
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

root_dir = os.path.dirname(os.path.abspath("__file__"))
root_dir = root_dir + "\IRR\example.xlsx"

print(root_dir)

df_data = pd.read_excel(root_dir)

#%%

x = df_data["年"]
y = df_data["年化報酬率"]

#%%

plt.figure(figsize=(10,6))
plt.style.use("ggplot") 
plt.plot(x,y,color="b",linewidth=2.0)
plt.title("IRR",fontsize = 20, fontweight = "bold")
plt.ylabel("IRR",fontsize = 15,fontweight = "bold")
plt.xlabel("year",fontsize = 15,fontweight = "bold")

plt.scatter(x,                      # x軸資料
            y,                      # y軸資料
            c = "r",                # 點顏色
            s = 50,                 # 點大小
            alpha = 1,              # 透明度
            marker = "D")           # 點樣式
plt.savefig("./IRR/IRR_example.jpg")        #儲存圖檔
plt.show

#%%



#%%
