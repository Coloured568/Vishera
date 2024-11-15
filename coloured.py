import vishera
import os
import random
import time
import sys

# version = "V1.0"
vishera.name = "CShell" 
# add these details if you plan on making a solid extension

'''def header():
    print("Coloured's Demo")''' # no need; vishera.header exists now

def about():
    vishera.output("Commands: \n" +
    
          "cpu() \n" +
         
         "system() \n" +

          "source() \n" +

          "date() \n" +

          "calc() \n" +

          "think() \n"


    )

def shell():
    prompt = input("Enter 'help' to view commands or type 'exit()' to quit: ")

    if prompt == "exit()":
        vishera.isRun = 0  
    elif prompt == "help":
        about()
    elif prompt == "cpu()":
        cpu()
    elif prompt == "system()":
        system()
    elif prompt == "source()":
        source()
    elif prompt == "date()":
        date()
    elif prompt == "calc()":
        print("Entering calculator... Please provide an equation.")
        run_calc()  # This is now triggered when the user types 'calc()' explicitly.
    elif prompt == "think()":
        think()
    else:
        print("Unknown command.")


# commands = {"cpu()", "ram()"}

def motd():
    messages = [
        "Much love to all the people in my life!",
        "GTX 1060 3GB FTW",
        "*Insert Minecraft reference*",
        "Does anyone read these?",
        "Don't forget to make frequent backups!",
        "14th gen Intel cpus <<<",
        "GTX 1070 finna be my next GPU trust",
        "I GOT THE GTX 1070!!!",
        "Intel Core i7-8700 is my best friend",
        "Don't generate E-waste! Turn your old computers into servers!",
        "Intel Core i3-3220 actually runs somewhat decent :D",
        "DDR4 is peak",
        "Imagine being Drake during the Kendrick beef XD",
        "Erik Houdini, if ur reading this, sign my guestbook rn",
        "i just lost my dawwwwwwg",
        "2025 is gonna be a great year for racing games",
        "balling so hard",
        "steal from greedy corporations!!!",
        "what do the hackers benefit from wrecking internet archives??",
    ]

    randmotd = messages[random.randint(0,17)]

    vishera.output(randmotd)
    # print(len(messages))

def cpu():
    '''
    or instead of outputting the actual machine details, you can hard code it like:
    core_count = 8
    '''
    core_count = os.cpu_count()
    vishera.output(f"{core_count} logical cores detected.")

def system():
    '''
    or instead of outputting the actual machine details, you can hard code it like:
    operating_system = "ColouredOS9"
    '''
    operating_system = os.name
    vishera.output(f"System: {operating_system}")

def source():
    vishera.output("GitHub repo coming soon!")

def date():
    print("MLA date formatter")

    day = int(input("Enter a day (1-31): "))
    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")
    
    month = int(input("Enter a month (1-12): "))
    if month == 4 and day == 31:
        print("Error. Day must be within the month.")
    if month == 6 and day == 31:
        print("Error. Day must be within the month.")
    if month == 9 and day == 31:
        print("Error. Day must be within the month.")
    if month == 11 and day == 31:
        print("Error. Day must be within the month.")
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
    
    year = int(input("Enter year: "))
    year_string = str(year)
    if len(year_string) != 4:
        print("Error. Year must have four digits.")
    
    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December']
    
    print("The day is:", day, month_name[month-1], year)
    
def calc(values):
    try:
        result = round(eval(values), 2)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

def user_define_function():
    func_name = input("Enter function name (e.g., f(x)): ")
    func_body = input(f"Enter the formula for {func_name}: ")
    # Store the user function as a callable expression
    globals()[func_name] = lambda x: eval(func_body)
    print(f"{func_name} has been defined.")

def run_calc():
    equation = input("Enter equation or 'define' to create a function: ")

    if equation == "define":
        user_define_function()
    else:
        calc(equation)

def thethinker():
    one_or_two = random.randint(1, 2)

    option_1 = input("Enter option 1: ")
    option_2 = input("Enter option 2: ") 
    
    print("\nLet me think for a second...\n")

    time.sleep(3)

    if one_or_two == 1:
        print(option_1)
    else:
        print(option_2)


def think():
    print("Welcome! Having trouble deciding?\n")
    print("Enter '1' to have me decide!")
    print("Enter '2' to exit the program.\n")

    user_input = input("Enter input: ")

    if user_input == '1': 
        thethinker()
    elif user_input == '2':
        print("Exiting the program.")
    else:
        print("Invalid input. Please enter '1' or '2'.")
