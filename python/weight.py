import time
### User entered data
startDate = (2019, 4, 29, 13, 3, 39, 0, 119, 1)  #year, month, day
endDate = (2019, 5, 29)  #year, month, day
startingWeight = 172
goalPerWeek = 2  #how many pounds you want to lose per week

goalPerDay = goalPerWeek/7
goalPerHour = goalPerDay/24

buffer = 1/24

currentWeight = int(input("Enter your current weight: "))

currentDate = time.localtime()

x = currentDate[3]
print(x)

requiredWeight = (startingWeight - (currentDate[7] - startDate[7])*goalPerDay) + buffer*currentDate[3] + (buffer/60)*currentDate[4]

if(currentWeight < requiredWeight):
    print("you can eat", currentWeight, requiredWeight)
else:
    print("you can not eat", currentWeight, requiredWeight)