import random
import math

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

#####################
#       Day 4       #
#####################
def Coin_Flip():
    coin_flip = random.randint(0,1)
    if coin_flip == 1:
        print("Heads")
    else:
        print("Tails")

def Banker_Roulette():
    names_string = "Bob, Jen, Larry, Moe, Curly, Leo, Monty" # 7
    names = names_string.split(", ")
    payer = random.randint(0, len(names) - 1)

    print(f"{names[payer]} is going to buy the meal today!")
    
#####################
#       Day 5       #
#####################
def avg_student_height():
    student_heights = input("Enter heights of students separated by a space:\n ").split()

    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    
    total_height = 0
    number_of_students = len(student_heights)
    for student in student_heights:
        total_height += student

    average_height = round(total_height / number_of_students)
    print(f"Total height: {total_height}")
    print(f"Number of students: {number_of_students}")
    print(f"The average height is {average_height}")

def add_even_numbers():
    target = int(input("Enter a number bewtween 0 and 1000: "))
    sum = 0
    for num in range(0, target + 1, 2):
        sum += num
    print(f"The sum of the numbers between 0 and {target} is {sum}")

def FizzBuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 3 != 0 and num % 5 == 0:
            print("Buzz")
        else:
            print(num)


#####################
#       Day 8       #
#####################
def greet(name, name2, name3):
    print(f"Hello {name}")
    print(f"Hello {name2}")
    print(f"Hello {name3}")

def paint_calc(height, width, cover=5):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"For a room that is {height}x{width}, you will need {number_of_cans} cans of paint.")

def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

#####################
#       Day 9       #
#####################
def Student_Grades_Calc():
    student_scores = {
        "Harry" : 81,
        "Ron"   : 78,
        "Hermione": 99,
        "Draco" : 74,
        "Neville": 64,
    }

    student_grades = {}

    print(student_scores["Draco"])

    for student in student_scores:
        if(student_scores[student] <= 70):
            student_grades[student] = "Fail"
        elif(student_scores[student] > 70 and student_scores[student] <= 80):
            student_grades[student] = "Acceptable"
        elif(student_scores[student] > 80 and student_scores[student] <= 90):
            student_grades[student] = "Exceeds Expections"
        elif(student_scores[student] > 90):
            student_grades[student] = "Outstanding"

    print(student_grades)

def add_new_country(country_name, num_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = num_visits
    new_country["cities"] = cities_visited
    
    travel_log.append(new_country)
