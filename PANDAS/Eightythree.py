import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "year": [2021, 2022, 2023, 2024],
    "profit": [50, 70, 120, 180]
})

df.plot(x="year", y="profit", kind="line", title="Yearly Profit")
plt.show()
