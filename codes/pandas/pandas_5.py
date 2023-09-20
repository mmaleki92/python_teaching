import pandas as pd

data = {"Name": ["John", "Alex", "Mary"],
        "Age": [25, 30, 27],
        "Country": ["USA", "Canada", "UK"]}
df = pd.DataFrame(data)
filtered = df[df["Age"] > 25]
print(filtered)