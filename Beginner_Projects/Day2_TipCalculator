def Tip_Calculator():
    print("Welcome to the tip calculator")
    bill_total = float(input("What was the total bill? $"))
    tip_percentage = float(input("What percent tip would you like to give? ")) / 100
    bill_split = int(input("How many people to split the bill? "))

    payment_amount = round((bill_total + (bill_total * tip_percentage)) / bill_split,2) 

    print(f"Each person should pay: ${payment_amount}.")

Tip_Calculator()