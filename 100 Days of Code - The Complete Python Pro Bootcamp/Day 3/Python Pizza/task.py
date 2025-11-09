"""print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")"""
"""weight = 85
height = 1.85
bmi = weight / (height ** 2)
print(f"your BMI is : \n{bmi}")
if bmi <= 18.5:
  print("Under weight")
elif 18.5 <= bmi < 25:
  print("Normal weight")
elif 25<= bmi > 30:
  print("Over weight")
else:
  print("Check it again")

weight = 85
height = 1.85
bmi = weight / (height ** 2)"""
weight = 85
height = 1.85
bmi = weight / (height ** 2)
y = round(int(bmi))
# 🚨 Do not modify the values above
# Write your code below 👇
print(f"your BMI is : {y}")
if y < 18.5:
    print("Under weight")
elif 18.5 <= y < 25:
    print("Normal weight")
elif 25 <= y < 30:
    print("Over weight")
else:
    print("Obese")





