import matplotlib.pyplot as plt
import numpy as np

x = range(2018, 2024)
y = [3,4,9,10,12,5]

fig, ax1 = plt.subplots()
ax2 = ax1
ax1.bar(x, y, color='b')
ax2.plot(x, y, color='r', marker='o')

ax1.set_ylabel('文献数量/篇')
ax1.set_xticklabels(["","2018年","2019年","2020年","2021年","2022年","2023年"])



plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.show()



