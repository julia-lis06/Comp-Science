#rainfall question
total_rainfall = 0
count_exceeded = 0
rainfall_list = []

for day in range(1,8):
    rainfall = float(input("Enter recorded rainfall for day {}:" .format(day)))
    rainfall_list.append(rainfall)
    total_rainfall += rainfall
    if rainfall > 3.5:
        count_exceeded +=1
        print("Day {}: Rainfall exceeded 3.5 by {} cm.".format(day,round(rainfall -3.5)))
    