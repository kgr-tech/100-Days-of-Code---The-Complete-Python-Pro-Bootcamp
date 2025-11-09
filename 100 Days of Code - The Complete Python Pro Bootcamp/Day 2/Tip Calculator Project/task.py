"""print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))"""
print("welcome to new era to my calculater!")
bill=float(input("what was the total bill? $ "))
percentage=int(input("how much tip would like to give?10 12 20?"))
u = percentage/100
split = int(input("how many people to split the bill?"))
total_tip_amount = (1 + percentage/100)
total_bill = (bill/split) * total_tip_amount
#split = int(input("how many people to split the bill?"))
total_amount = int(round(total_bill, 2))
print(f" Each person should pay : $ {total_amount}")
print(150+(1+12/100))
print(12/100)
