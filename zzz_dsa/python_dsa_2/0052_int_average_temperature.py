days = int(input("enter no of days: "))
total = 0
for i in range(days):
    temp = input(f"enter day {i+1}'s temp: ")
    total += int(temp)
average = round(total/days, 2)
print(f"average: {average}")