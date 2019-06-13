import numpy as np
from my_module.functions import *

print('Hey! I will be helping you calculate your grade or GPA.')
print('')

while True:     # Asks the user what they would like to calculate.
    # Will run only if 'gpa' or 'grade' is in the user's input (whichever comes first)

    choice = input('Which would you like to calculate? :')

    if 'grade' in choice.lower():
        print('')
        print("No problem! I'll just need some information")
        print('')

        run = GradeCalculator()    # Creates instance of grade calculator class
        run.find_categories()     # Gets the number of categories from the user
        run.grade_weights()    # Gets the grade and weight of each category
        run.grade_calculator()    # Calculates the total percentage

        print('Your grade is', "%.2f" % run.total, '%')  # https://stackoverflow.com/a/3914795
        break

    elif 'gpa' in choice.lower():
        print('')
        print("Okay! Let's get started")
        print('')
        run = GpaCalculator()    # Creates instance of GPA Calculator class
        run.find_grades_units()    # Gets the letter grade and units from the user
        run.grade_converter()    # Converts the letter grade to a number
        total_grade_points = run.total_num_calc()
        total_units = run.add_num(run.units)    # Units added together
        gpa = total_grade_points / total_units
        print('Your GPA is', "%.3f" % gpa)  # https://stackoverflow.com/a/3914795
        break
    else:
        print("Oops! I'm sorry I don't understand. Please type in 'grade' or 'GPA'")
        print('')
        pass
