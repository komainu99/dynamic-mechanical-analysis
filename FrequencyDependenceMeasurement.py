%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/yazuhidekazu/Library/CloudStorage/OneDrive-KyushuUniversity/研究/220701_Rheo/100mg03%10to500rads (2).txt'
file_path2 = '/Users/yazuhidekazu/Library/CloudStorage/OneDrive-KyushuUniversity/研究/220701_Rheo/50mg03%10to500rads (3).txt'
file_path3 = '/Users/yazuhidekazu/Library/CloudStorage/OneDrive-KyushuUniversity/研究/220701_Rheo/25mg03%10to500rads (2).txt'
file_path4 = '/Users/yazuhidekazu/Library/CloudStorage/OneDrive-KyushuUniversity/研究/220701_Rheo/25mg03%10to500rads (4).txt'
file_path5 = '/Users/yazuhidekazu/Library/CloudStorage/OneDrive-KyushuUniversity/研究/220701_Rheo/25mg03%10to500rads (5).txt'

column = 'Tan(delta)'

df = pd.read_table(file_path, header=90)
df.drop(index=0, inplace=True)

df2 = pd.read_table(file_path2, header=90)
df2.drop(index=0, inplace=True)

df3 = pd.read_table(file_path3, header=90)
df3.drop(index=0, inplace=True)

df4 = pd.read_table(file_path4, header=90)
df4.drop(index=0, inplace=True)

df5 = pd.read_table(file_path5, header=90)
df5.drop(index=0, inplace=True)

#print(df["Storage modulus"])

fig, ax = plt.subplots()

plt.plot(df['Angular frequency'].astype('float'), df[column].astype('float'), label='100mg/mL', marker='x', linestyle='None')
plt.plot(df2['Angular frequency'].astype('float'), df2[column].astype('float'), label='50mg/mL', marker='v', linestyle='None')
plt.plot(df3['Angular frequency'].astype('float'), df3[column].astype('float'), label='25mg/mL', marker='.', linestyle='None')
#plt.plot(df4['Angular frequency'].astype('float'), df4['Storage modulus'].astype('float'), label='25mg/mL', marker='.', linestyle='None')
#plt.plot(df5['Angular frequency'].astype('float'), df5['Storage modulus'].astype('float'), label='25mg/mL', marker='.', linestyle='None')
#plt.plot(df['Angular frequency'].astype('float'), df['Storage modulus'].astype('float'), label="Storage modulus", marker='v', linestyle='None')

ax.set_yscale('log')
ax.set_xlim(10,550)
ax.set_ylim(0.001,3)

ax.set_xlabel('Angular frequency[rad/s]')
ax.set_ylabel("%s"%column)

title = column

plt.legend(bbox_to_anchor=(1, 0), loc='lower right', borderaxespad=1)
plt.show()

fig.savefig("%s.png"%title)