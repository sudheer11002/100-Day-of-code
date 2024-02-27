print("Welcome to the top calculatoer.")

bill_amount = float(input("What was the total bill? "))

tip= int(input("What persantage tip would you like to give? 10, 12 or 15:  "))

total_person = int(input("How many people to split the bill?  "))

total= tip/100 * bill_amount +bill_amount

print(f"Each person should pay: {total}")
