# Health and fitness calculator to practice functions and list.
def calculate_bmi(weight, height_cm):
    height_m= height_cm/100
    bmi = weight/(height_m**2)
    return bmi

def classify_bmi(bmi):
    if bmi <= 18.4:
      return('underweight')
    elif bmi >= 18.5 and bmi <= 24.9:
      return(' health weight')
    elif bmi >= 25 and bmi <= 29.9:
      return('overweigth')
    else: 
      return("obese")

def run_bmi_calculator():
    weight = float(input("What is your weight in kg?"))
    height_cm = float(input ("What is yoour height in cm?"))
    bmi_value = calculate_bmi(weight,height_cm)
    bmi_category = classify_bmi(bmi_value)
    print(round(bmi_value,2))
    print(bmi_category)

def main():
    while True:
         print("What would you like to do?")
         print("Press 1 for calculating BMI")
         print("Press 2 to quit")
         choice= input("Choose option: ")

         if choice=="1":
            run_bmi_calculator()
         elif choice=="2":
            print("Bye")
            break
         else:
            print("Please choose one of the options")
    
main()
   