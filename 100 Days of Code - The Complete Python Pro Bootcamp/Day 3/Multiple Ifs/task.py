print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")




"""print("Welcome to BMI calculater")
input("Are you ready to proceed?\n")
W = float(input("please could you enter your weight?\n"))
H = float(input("Enter you're present height?\n"))
Bmi = W / (H**2)
X = round(Bmi)
print(f" your BMI is : {X}")
if X <= 18.5:
  print("Underweight")
elif 18.5<= X < 25:
  print("Normal weight")
elif 25<= X > 30:
  print("overweight")
else:
    print("check it again")"""


