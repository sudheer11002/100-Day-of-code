print("Welcome to the top calculatoer.")

bill_amount = int(input("What was the total bill? "))

tip= int(input("What persantage tip would you like to give? 10, 12 or 15:  "))

total_person = int(input("How many people to split the bill?  "))

total= tip/bill_amount/total_person

print(total)

print("Each person should pay: ")
