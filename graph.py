#!/usr/bin/env python3
import oursql
import yaml
f = open("database.yml", 'r')
db = yaml.load(f)
f.close()

import pandas as pd
import matplotlib as plt
plt.use('Agg')

# df = pd.read_csv("tsl_graph/luxes.csv")
conn = oursql.connect(
        host=db["host"],
        port=db["port"],
        db=db["name"],
        user=db["user"],
        passwd=db["pass"])
cur = conn.cursor()
sql = "select recorded_at, lux from luxes order by recorded_at desc"

# cur.execute(sql)
# res = cur.fetchall()
df = pd.read_sql(sql,conn)

df.plot(x='recorded_at')
plt.pyplot.savefig("luxes.png")
