import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "customer_id": [1, 2, 3, 4],
    "Ranks": ["first", "second", "third", "fourth"],
    "fruits": ["orange", "apple", "pineapple", "watermelon"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

label_encoder = LabelEncoder()
df["fruits"] = label_encoder.fit_transform(df["fruits"])
df["Ranks"] = label_encoder.fit_transform(df["Ranks"])

print("\nDataFrame after encoding ranks with custom order:")
print(df)
