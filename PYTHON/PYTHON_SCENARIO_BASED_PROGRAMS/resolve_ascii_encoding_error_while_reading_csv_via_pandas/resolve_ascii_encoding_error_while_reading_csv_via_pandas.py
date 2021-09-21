# not tested with actual unicode characters

import pandas as pd

df = pd.read_csv("C:/REPOSITORIES/MyRepo/PYTHON/PYTHON_SCENARIO_BASED_PROGRAMS/resolve_ascii_encoding_error_while_reading_csv_via_pandas/sample.csv", encoding="utf-8")
print(df)
