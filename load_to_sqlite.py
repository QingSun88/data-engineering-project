import sqlite3
import pandas as pd

# connect database
conn = sqlite3.connect("weather.db")

# read csv
df = pd.read_csv("data/csv/weather_2026-05-15.csv")

# load into database
df.to_sql("weather", conn, if_exists="append", index=False)

print("Data loaded successfully!")

conn.close()
