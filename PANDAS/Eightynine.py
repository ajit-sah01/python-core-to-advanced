import pandas as pd

data = pd.DataFrame({
    "region": ["East", "East", "West", "West"],
    "product": ["A", "B", "A", "B"],
    "sales": [1000, 1500, 1200, 1800]
})

pivot = pd.pivot_table(
    data,
    values="sales",
    index="region",
    columns="product",
    aggfunc="sum"
)

print(pivot)
