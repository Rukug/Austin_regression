import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("austin_home_sales.csv")

print(df.shape)

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.6f}".format)
print(df.describe())

plt.scatter(df["Sq_Footage"], df["Sale_Price"])
plt.xlabel("Sq_Footage")
plt.ylabel("Sale_Price")
plt.savefig("scatter.png")
