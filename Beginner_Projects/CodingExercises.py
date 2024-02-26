def BMI_Calc():
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))

    BMI = int(weight / (height ** 2))

    print(f"Your BMI is {BMI}%")

def Life_In_Weeks():
    age = int(input("Enter your age in years: "))
    user_age_in_weeks = age * 52

    max_age_in_weeks = 90 * 52

    print(f"You have {max_age_in_weeks - user_age_in_weeks} weeks left.")
