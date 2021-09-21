days = int(input("enter no of days: "))
total = 0
all = []
for i in range(days):
    temp = input(f"enter day {i+1}'s temp: ")
    total += int(temp)
    all.append(int(temp))
average = round(total/days, 2)
print(f"average: {average}")

above = 0
for i in all:
    if i > average:
        above += 1
print(f"{above} days above avg")
