with open("C:/REPOSITORIES/MyRepo/PYTHON/PYTHON_SCENARIO_BASED_PROGRAMS/add_new_line_on_top_of_csv/sample.csv", "r") as f:
    content = f.readlines()
with open("C:/REPOSITORIES/MyRepo/PYTHON/PYTHON_SCENARIO_BASED_PROGRAMS/add_new_line_on_top_of_csv/sample.csv", "w") as f:
    f.writelines([content[0]] + ["0,0,0\n"] + content[1:])
