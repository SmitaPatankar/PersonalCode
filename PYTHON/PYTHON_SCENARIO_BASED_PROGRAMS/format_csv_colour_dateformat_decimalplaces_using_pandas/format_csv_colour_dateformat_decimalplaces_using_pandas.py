import pandas as pd

df = pd.read_csv("C:/REPOSITORIES/MyRepo/PYTHON/PYTHON_SCENARIO_BASED_PROGRAMS/format_csv_colour_dateformat_decimalplaces_using_pandas/sample.csv")
print("----------------original----------------")
print(df)

# format color - not tested
def color_red_or_green(val):
    color = 'red' if val <= 1 else 'green'
    return 'color: %s' % color
s = df.style.applymap(color_red_or_green)
print("----------------coloured----------------")
s

# format decimal places
print("----------------rounded----------------")
print(df.round(2))

# format datetime format
df["b"] = pd.to_datetime(df["b"]).dt.strftime('%Y-%m-%d')
print("----------------datetimeformatted----------------")
print(df)