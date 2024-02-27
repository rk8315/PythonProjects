#####################
#       Day 2       #
#####################

def BMI_Calc():
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))

    BMI = int(weight / (height ** 2))

    print(f"Your BMI is {BMI}")

def Life_In_Weeks():
    age = int(input("Enter your age in years: "))
    user_age_in_weeks = age * 52

    max_age_in_weeks = 90 * 52

    print(f"You have {max_age_in_weeks - user_age_in_weeks} weeks left.")


#####################
#       Day 3       #
#####################
def Odd_or_Even():
    number = int(input("Enter an integer: "))
    if (number % 2 == 0):
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")

def BMI_Calc_2dot0():
    height = float(input("Enter your height in meters: "))
    weight = int(input("Enter your weight in kilograms: "))
    BMI = int(weight / (height ** 2))
    if(BMI <= 18.5):
        print(f"Your BMI is {BMI}, you are underweight.")
    elif(BMI > 18.5 and BMI < 25):
        print(f"Your BMI is {BMI}, you have normal weight.")
    elif(BMI >= 25 and BMI < 30):
        print(f"Your BMI is {BMI}, you are slightly overweight.")
    elif(BMI >= 30 and BMI < 35):
        print(f"Your BMI is {BMI}, you are obese.")
    elif(BMI >=35):
        print(f"Your BMI is {BMI}, you are clinically obese.")

def Auto_Pizza_Order():
    print("Welcome to Python Pizza Deliveries")
    size = input("What size pizza do you want? (S, M, L): ").lower()
    add_pepperoni = input("Do you want pepperoni? (Y or N): ").lower()
    extra_cheese = input("Do you want extra cheese? (Y or N): ").lower()
    final_bill = 0

    if(size == "s"):
        final_bill += 15
    elif(size == "m"):
        final_bill += 20
    elif(size == "l"):
        final_bill += 25
    else:
        print("Invalid size selection.")

    if(add_pepperoni == "y"):
        if(size == "s"):
            final_bill += 2
        else:
            final_bill += 3
    
    if(extra_cheese == "y"):
        final_bill  +=1

    print(f"Your final bill is: ${final_bill}.")

