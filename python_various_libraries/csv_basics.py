import csv
csv_file = "abc.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["id", "name"])
    for values in [[1,"smita"], [2,"neha"]]:
        csv_writer.writerow(values)

# id,name
# 1,smita
# 2,neha
