import time
print("Welcome to Temperature Scale")
print("Developed by Rudra")
#Greeting
user_name = input("Enter your name: ")
hour = int(time.strftime("%H"))
if (hour>= 3 and hour< 12):
    print("Good Morning", user_name)
elif (hour>= 12 and hour< 17):
    print("Good Afternoon", user_name)
else:
    print("Good Evening", user_name)
#Temperature Scale
print("Press 1 to convert Celsius to Kelvin\nPress 2 to convert Kelvin to Celsius\nPress 3 to convert Celsius to Fahrenheit\nPress 4 to convert Fahrenheit to Celsius\nPress 5 to convert Fahrenheit to Kelvin\nPress 6 to convert Kelvin to Fahrenheit")
user_choice = int(input("Choose your Converter: "))
if (user_choice == 1):
    unit1_x = float(input("Enter value: "))
    unit1_y = unit1_x+273.15
    print(unit1_x, " Celsius is ", unit1_y, " Kelvin")
elif (user_choice == 2):
    unit2_x = float(input("Enter value: "))
    unit2_y = unit2_x-273.15
    print(unit2_x, " Kelvin is ", unit2_y, " Celsius")
elif (user_choice == 3):
    unit3_x = float(input("Enter value: "))
    unit3_y = unit3_x*9/5
    unit3_z = unit3_y+32
    print(unit3_x, " Celsius into Fahreneit is ", unit3_z, " Fahrenheit")
elif (user_choice == 4):
    unit4_x = float(input("Enter value: "))
    unit4_y = unit4_x-32
    unit4_z = unit4_y*5/9
    print(unit4_x, " Fahrenheit into Celsius is ", unit4_z, " Celsius")
elif (user_choice == 5):
    unit5_x = float(input("Enter value: "))
    unit5_y = unit5_x-32
    unit5_z = unit5_y*5/9
    unit5_a =unit5_y+273.15
    print(unit5_x, " Fahrenheit into Kelvin is ", unit5_z, " Kelvin")
elif (user_choice == 6):
    unit6_x = float(input("Enter value: "))
    unit6_y = unit6_x-273.15
    unit6_z = unit6_y*9/5
    unit6_a = unit6_z+32
    print(unit6_x, " Kelvin into Fahrenheit is ", unit6_a, " Fahrenheit")
else:
    print("Invalid Input")
print("Developed By Rudra")
print("My Site = https://rudrasworld.infinityfreeapp.com")