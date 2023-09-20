import pandas as pd

data = {"Name": ["John", "Alex", "Mary"],
        "Age": [25, 30, 27],
        "Country": ["USA", "Canada", "UK"]}
df = pd.DataFrame(data)
df = df.rename(columns={"Name": "Full Name", "Country": "Nation"})
print(df)
