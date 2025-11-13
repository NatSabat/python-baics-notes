weight = float(input("What is your weight in kg?"))
height = float(input ("What is yoour height in cm?"))

value_1 = height/100.0

value_2 = weight / (value_1 **2 )

result = value_2

if result <= 18.4:
    print('You are underweight')
elif result >= 18.5 and result <= 24.9:
    print('You have health weight')
elif result >= 25 and result <= 29.9:
    print('You are overweigth')
else: 
    print("You are obese")

