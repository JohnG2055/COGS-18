import numpy as np

        
class GradeCalculator:
    """
    This class contains methods that gets the number of categories and percentages
    from the user. It then multiplies each category with its respective percentage and
    calculates the overall grade
    """

    percentage_list = []
    weight_list = []
    multiplied_list = []
    total = 0
    num_categories = 0

    def find_categories(self):

        """Asks the user how many categories are used when calculating the final grade"""

        while True:  # Continues to ask the user for the number of categories until an integer is given
            try:
                start = int(input('Please enter the number of categories: '))
                self.num_categories += start
                print('')
                break
            except ValueError:  # https://docs.python.org/3.1/library/exceptions.html#bltin-exceptions
                print('Please enter an integer!')
                print('')
                pass

    def grade_weights(self):

        """
        This method gets the number of categories, the weight of each category,
        and the grade of the user in each category

        Weight is converted to number between 0 and 1 and appended to an empty list

        Percentage is appended to an empty list
        """

        class_num = 1

        for num in range(self.num_categories):
            if class_num == 1:
                ending = 'st'
            elif class_num == 2:
                ending = 'nd'
            elif class_num == 3:
                ending = 'rd'
            else:
                ending = 'th'

            while True:
                try:
                    weight = float(input('Enter the weight of the ' + str(class_num)
                                         + ending + ' category: '))
                    new_weight = weight * 0.01  # Multiplies the weight by 0.01 to get a value between 0 and 1
                    self.weight_list.append(new_weight)
                    break
                except ValueError:
                    print('Please enter an integer!')
                    print('')
                    pass

            while True:
                try:
                    percentage = float(input('What percentage do you have in this category? '
                                             '(Please enter an integer) '))
                    self.percentage_list.append(percentage)
                    print('')
                    break
                except ValueError:
                    print('Please enter an integer!')
                    print('')
                    pass

            class_num += 1

    def grade_calculator(self):

        """
        This method gets the converted weight and multiplies this new value with the corresponding percentage.

        The new values are then summed up
        """

        for weight, grade in zip(self.weight_list, self.percentage_list):
            self.multiplied_list.append(weight * grade)  # Multiplies weight with percentage

        for multiplied_grade in self.multiplied_list:  # Adds the previously calculated numbers together
            self.total += multiplied_grade


class GpaCalculator:
    """
    This class contains methods that asks the user to input grades and units for each
    class. It then uses that information to calculate the GPA
    """

    class_num = 1
    num_total = 0
    grades = []
    units = []
    grade_num = []
    grade_to_num = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                       'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0}

    def find_grades_units(self):

        """
        Asks the user for the total number of classes. Then asks the user to input the grade and number
        of units for each class and appends them to their own list
        """

        while True:
            try:
                num_of_classes = int(input('Number of classes: '))
                print('')
                break
            except ValueError:
                print('Please enter an integer!')
                print('')
                pass

        for grade in range(num_of_classes):

            if self.class_num == 1:
                ending = 'st'
            elif self.class_num == 2:
                ending = 'nd'
            elif self.class_num == 3:
                ending = 'rd'
            else:
                ending = 'th'

            letter_grade = input('Please enter the grade of the ' + str(self.class_num) + ending + ' class: ')

            if letter_grade.upper() in self.grade_to_num.keys():
                self.grades.append(letter_grade.upper())
                self.class_num += 1
            else:
                while letter_grade.upper() not in self.grade_to_num.keys():
                    print('I think you may have input the grade incorrectly')
                    print('')
                    letter_grade = input('Please enter the grade of the ' + str(self.class_num) + ending + ' class: ')

                self.grades.append(letter_grade.upper())
                self.class_num += 1

            while True:
                try:
                    class_unit = float(input('Please enter the number of units for this class: '))
                    print('')
                    self.units.append(class_unit)
                    break
                except ValueError:
                    print('Please enter a number!')
                    print('')
                    pass

    def grade_converter(self):

        """Takes in a list of grades given by the user, converts the grade to the corresponding number, and appends
        it to an empty list"""

        for item in self.grades:
            self.grade_num.append(self.grade_to_num[item])

    def total_num_calc(self):

        """
        Multiplies the each item of two lists together and appends them to a new list (total_num_list).

        Then every item in total_num_list gets added together.

        Returns
        -------
        num_sum : float
            The sum of all values in total_num_list
        """

        num_sum = 0

        new_units = np.array(self.units, dtype=float)
        # https://kite.com/python/examples/43/numpy-construct-an-array-of-%60float%60s

        new_grade_num = np.array(self.grade_num, dtype=float)

        total_num_list = np.ndarray.tolist(new_units * new_grade_num)
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html

        for num in total_num_list:
            num_sum += num

        return num_sum

    def add_num(self, num):

        """
        Adds all of the numbers in a list together and outputs a number

        Parameters
        ----------
        num : list
            A list of units created by the user when the 'find_grade_units()' method is called.

        Returns
        -------
        num_total : float
            The sum of the numbers in the given list
        """

        for point in num:
            self.num_total += point

        return self.num_total
