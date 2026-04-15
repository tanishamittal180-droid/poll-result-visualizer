import pandas as pd

df = pd.read_csv("data/poll_data.csv")

df = df.drop_duplicates()
df = df.dropna()

df['Preferred_Tool'] = df['Preferred_Tool'].str.strip().str.title()

df.to_csv("data/cleaned_poll_data.csv", index=False)

print("Data cleaned!")