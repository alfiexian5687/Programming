print("Electricity bill estimator")
centskwh=float(input("Enter cents per KWh: "))
dailyuse=float(input("Enter daily use in KWh: "))
numdays=int(input("enter number of billing days: "))
totalbill=centskwh*dailyuse*numdays/100
print("Estimate bill: $",totalbill)
