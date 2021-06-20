# not tested with actual unicode characters

import pandas as pd

df = pd.read_csv("C:/REPOSITORIES/MyRepo/python/python_scenario_based_programs/resolve_ascii_encoding_error_while_reading_csv_via_pandas/sample.csv", encoding="utf-8")
print(df)
