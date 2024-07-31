import pandas as pd
import matplotlib.pyplot as plt

# データの読み取り
# 課題によってカラムの名前を変える
#column_names = ['AdvCost', 'Profit', 'a', 'b', 'c', 'd'] # (d)と(e)のカラム
#column_names = ['Member', 'Profit', 'a', 'b', 'c', 'd'] # (f)のカラム
#column_names = ['CostA', 'Profit', 'a', 'b', 'c', 'd'] # (g)のカラム
column_names = ['CostA', 'CostC', 'Profit', 'a', 'b', 'c', 'd'] # (h)のカラム

# 課題によって読み込むファイルを変える
data = pd.read_csv('results_h.txt', names=column_names)

plt.figure(figsize=(12, 6))

# 利益の変化
# カラムによって変わる
plt.subplot(1, 2, 1)
plt.plot(data["CostA"], data["Profit"], marker='o', label='Profit')
plt.xlabel('CostA')
plt.ylabel('Profit')
plt.title('Profit & CostA')
plt.grid(True)
plt.legend()

# 各変数の最適解の変化
# カラムによって変わる
plt.subplot(1, 2, 2)
plt.plot(data['Profit'], data['a'], marker='o', label='a')
plt.plot(data['Profit'], data['b'], marker='o', label='b')
plt.plot(data['Profit'], data['c'], marker='o', label='c')
plt.plot(data['Profit'], data['d'], marker='o', label='d')
plt.xlabel('Profit')
plt.ylabel('Optimal Values')
plt.title('Optimal Values & Profit')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

