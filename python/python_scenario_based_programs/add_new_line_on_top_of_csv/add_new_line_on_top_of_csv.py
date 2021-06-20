with open("C:/REPOSITORIES/MyRepo/python/python_scenario_based_programs/add_new_line_on_top_of_csv/sample.csv", "r") as f:
    content = f.readlines()
with open("C:/REPOSITORIES/MyRepo/python/python_scenario_based_programs/add_new_line_on_top_of_csv/sample.csv", "w") as f:
    f.writelines([content[0]] + ["0,0,0\n"] + content[1:])
