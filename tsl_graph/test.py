import pandas as pd
import matplotlib as plt
plt.use('TkAgg')

df = pd.read_csv('luxes.csv')
# df.index = pd.to_datetime(df.index)
df.plot(x='datetime')

# plt.pyplot.show()
plt.pyplot.savefig("luxes.png")
