print("welcome to the rollercoaster")
height = int(input("Waht is your hight in cm? "))

if height > 120:
    age = int(input("Waht is your age? "))
    if age<=12:
     print("Please pay $10")
    elif age<=18:
       print("Please pay $15") 
    else:
     print("Please pay $20")
else:
    print("Sorry, you have to grow taller before you can ride.")