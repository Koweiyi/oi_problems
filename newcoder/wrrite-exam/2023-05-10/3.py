import matplotlib.pyplot as plt
import numpy as np

x = range(2018, 2024)
y = [3,4,9,10,12,5]

fig, ax1 = plt.subplots()
ax2 = ax1
ax1.bar(x, y, color='b')
ax2.plot(x, y, color='r', marker='o')

ax1.set_ylabel('��������/ƪ')
ax1.set_xticklabels(["","2018��","2019��","2020��","2021��","2022��","2023��"])



plt.rcParams['font.sans-serif']=['SimHei'] #����������ʾ���ı�ǩ
plt.rcParams['axes.unicode_minus'] = False #����������ʾ����
plt.show()



