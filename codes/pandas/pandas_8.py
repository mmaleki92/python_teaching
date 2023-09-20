import pandas as pd

data = {"Name": ["John", "Alex", "Mary", "Peter"],
        "Age": [25, 30, None, 27],
        "Country": ["USA", "Canada", "UK", None]}
df = pd.DataFrame(data)
df = df.fillna("Unknown")
print(df)