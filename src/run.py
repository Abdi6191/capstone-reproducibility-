import pandas as pd

df = pd.read_csv("data/sample.csv")

precision = df["tp"].sum() / (df["tp"].sum() + df["fp"].sum())

with open("docs/metric.txt", "w") as f:
    f.write(f"precision={precision:.2f}\n")

print("Done. Output saved to docs/metric.txt")
