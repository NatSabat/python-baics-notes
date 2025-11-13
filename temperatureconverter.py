unit= float(input("To change temperature choose one of the options: 1. From Celsius to Fahrenheit or  2. From Fahrenheit to Celsius "))

if unit == 1 :
   temp_1 = float(input("What is the temperature in Celsius?"))
   resut_1 = (temp_1*1.8) + 32 
   print(resut_1, "F")
elif unit == 2:
   temp_2= float(input("What is the temperature in Fahrenheit"))
   result_2= (temp_2 -32)/1.8
   print(result_2 ,"C")
else:
    print("Choose from option 1 or 2 ! ")

