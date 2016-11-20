#!/usr/bin/env python
import pandas as pd
import matplotlib as plt
plt.use('Agg')

df = pd.read_csv("tsl_graph/luxes.csv")
# df.index = pd.to_datetime(df.index)
df.plot(x='datetime')

# plt.pyplot.show()
plt.pyplot.savefig("tsl_graph/luxes.png")
