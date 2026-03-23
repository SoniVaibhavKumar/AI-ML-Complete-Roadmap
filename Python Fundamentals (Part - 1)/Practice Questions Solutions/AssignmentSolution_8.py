principle = float(input("Enter principle amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

SI = (principle * time * rate) / 100

print("Simple Interest = ",SI)