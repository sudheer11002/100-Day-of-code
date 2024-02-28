year = int(input("Enter your birth year to check it was the leap year : "))

if year % 4== 0:
    # do something
    if year % 100 ==0:
        #do something
        print()
        if year % 400 == 0:
            print("Waaoo, you were born in leap year !!")
    else:
        print("Waaoo, you were born in leap year !!")   
else:
    print("Ohhh... the year you born was not the leap year !!")