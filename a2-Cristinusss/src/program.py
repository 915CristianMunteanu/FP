#
# Write the implementation for A2 in this file
#

####################################################################### UI section ##################################################################
from math import sqrt


def print_menu_options():
    """

    This is a UI function that is used to show the user what options he has.

    :return:This function doesnt return anything.
    """
    print("If you want to add other complex numbers press 1 - \n"
          "If you want to display all the complex numbers in the program press 2 - \n"
          "If you want to see the sequence that contains the most numbers with at most 3 distinct values press 3 - \n"
          "If you want to see the sequence that contains the most numbers with the same modulus press 4 - \n"
          "If you want to exit press 5 - ")


def read_user_option():
    """

    This is a UI function that is used to read the option given by the user.

    :return: This function returns the option given by the user, which is a natural number (1,2,3,4,5). If the users gives another value, the functions returns None.
    """
    user_option = int(input("What is your option ? - "))
    if user_option > 5 or user_option < 1:
        return None
    else:
        return user_option


def ui_add_complex_number(list_of_complex_numbers):
    """

    This is a UI function that is used to read the real and imaginary part of a complex number. Then the function access other function (add_complex_number) that adds the given numbers to the list_of_complex_numbers.

    :param list_of_complex_numbers:
    :return:
    """
    how_many_numbers_to_add = int(input("How many numbers you want to add in the list of complex numbers? "))
    for index in range(0, how_many_numbers_to_add):
        real = int(input("Give the real part "))
        imag = int(input("Give the imaginary part "))
        add_complex_number(list_of_complex_numbers, real, imag)


def write_complex_number(real, imag):
    """

    This is a UI function that is used to write a complex number in the form Z = a + bi, where a is the real part and b is the imaginary part.

    :param real: Integer number
    :param imag: Integer number
    :return:
    """
    if real == 0:
        print("Z = " + str(imag) + "i")
    else:
        if imag == 0:
            print("Z = " + str(real))
        else:
            if imag > 0:
                print("Z = " + str(real) + "+" + str(imag) + "i")
            else:
                print("Z = " + str(real) + str(imag) + "i")


def ui_display_all_complex_number(list_of_complex_numbers):
    """

    This function is used to display all the complex numbers in list_of_complex_numbers. With the help of the function write_complex_number, it shows the number in the form Z = a + bi.

    :param list_of_complex_numbers: Its an array of dictionaries.
    :return:
    """

    for index in range(0, len(list_of_complex_numbers)):
        write_complex_number(get_real(list_of_complex_numbers[index]), get_imag(list_of_complex_numbers[index]))


def ui_display_sequence_with_at_most_3values(list_of_complex_numbers):
    """
       This is a UI function that is used to display the sequence created by the function get_sequence_with_at_most_3values
       :param list_of_complex_numbers: Its a list of dictionary, which contains integer values.
       :return: The function doesnt return anything, but it uses the function write_complex_number to display the numbers.
    """
    sequence_with_at_most_3values = get_longest_sequence_with_at_most_3_distinct_values(list_of_complex_numbers)
    for index in range(0, len(sequence_with_at_most_3values)):
        write_complex_number(get_real(sequence_with_at_most_3values[index]),
                             get_imag(sequence_with_at_most_3values[index]))


def ui_display_sequence_with_same_modulus(list_of_complex_numbers):
    """
    This is a UI function that is used to display the sequence created by the function get_sequence_with_same_modulus
    :param list_of_complex_numbers: Its a list of dictionary, which contains integer values.
    :return: The function doesnt return anything, but it uses the function write_complex_number to display the numbers.
    """
    sequence_with_same_modulus = get_sequence_with_same_modulus(list_of_complex_numbers)
    for index in range(0, len(sequence_with_same_modulus)):
        write_complex_number(get_real(sequence_with_same_modulus[index]), get_imag(sequence_with_same_modulus[index]))


##################################################################### Function section ################################################################

def get_real(complex_number):
    """

    This function is used to get just the real part of a complex number.

    :param complex_number: Is a dictionary.
    :return: Returns an integer number, the real part of the complex number.
    """
    return complex_number['real']


def get_imag(complex_number):
    """

    This function is used to get just the imaginary part of a complex number.

    :param complex_number: Is a dictionary.
    :return: Returns an integer number, the real part of the complex number.
    """
    return complex_number['imag']


def calculate_modulus(complex_number):
    """

    This function calculates the modulus of a given complex number (which is a dictionary).

    :param complex_number: Dictionary of integer values
    :return: Positive real number.
    """
    return sqrt(
        get_real(complex_number) * get_real(complex_number) + get_imag(complex_number) * get_imag(complex_number))


def run_menu():
    """

    THis is the function that runs the program. there is initialized the list_of_complex_numbers with 10 values.

    :return:
    """
    list_of_complex_numbers = [{'real': 1, 'imag': -2}, {'real': -1, 'imag': -2},
                               {'real': 4, 'imag': 1}, {'real': 4, 'imag': 1}, {'real': 7, 'imag': 7},
                               {'real': 7, 'imag': 7},
                               {'real': 0, 'imag': -2}, {'real': 0, 'imag': -2}, {'real': 0, 'imag': -2},
                               {'real': 9, 'imag': 0}]
    dictionary_of_options_for_menu = {1: ui_add_complex_number, 2: ui_display_all_complex_number,
                                      3: ui_display_sequence_with_at_most_3values,
                                      4: ui_display_sequence_with_same_modulus}

    while True:
        print_menu_options()
        user_option = read_user_option()
        if user_option == 5:
            break
        dictionary_of_options_for_menu[user_option](list_of_complex_numbers)


def create_complex_number(real, imag):
    """

    This function is used to convert the 2 given integer values( real, imag) into a complex number, which is a dictionary.

    :param real: Integer number
    :param imag:  Integer number
    :return: It returns a dictionary, a complex number, where a and b are integer values.
    """
    return {'real': real, 'imag': imag}


def add_complex_number(list_of_complex_numbers, real, imag):
    """

    This function adds a complex number to the list_of_complex_numbers.

    :param list_of_complex_numbers: Its a list of dictionaries, which contains integer values.
    :param real: Integer number
    :param imag: Integer number.
    :return:
    """
    complex_number = create_complex_number(real, imag)
    list_of_complex_numbers.append(complex_number)


def get_longest_sequence_with_at_most_3_distinct_values(list_of_complex_numbers):
    """

    Given a list_of_complex_numbers returns the largest sequence with at most 3values.

    :param list_of_complex_numbers: Its a list of dictionaries, which contains integer values.
    :return: The function returns a list which contains the sequence with the most numbers with at most 3 values
    """
    start_of_sequence_max = 0
    end_of_sequence_max = 0
    maximum_length = 0
    index = 0
    while index < len(list_of_complex_numbers) - 3:
        start_of_sequence = index
        end_of_sequence = index
        different_values = 1
        index_of_potential_list = index + 1
        if len(list_of_complex_numbers) - (index + 1) < maximum_length:
            index = len(list_of_complex_numbers)
        while index_of_potential_list < len(list_of_complex_numbers):
            if list_of_complex_numbers[start_of_sequence:index_of_potential_list:].count(list_of_complex_numbers[index_of_potential_list]) == 0:
                if different_values == 3:
                    index_of_potential_list = len(list_of_complex_numbers)
                else:
                    different_values += 1
                    end_of_sequence = index_of_potential_list
            else:
                end_of_sequence = index_of_potential_list
            if maximum_length < end_of_sequence - start_of_sequence:
                maximum_length = end_of_sequence - start_of_sequence
                start_of_sequence_max = start_of_sequence
                end_of_sequence_max = end_of_sequence
            index_of_potential_list += 1
        index += 1
    sequence_of_numbers_with_at_most_3values=list_of_complex_numbers[start_of_sequence_max:end_of_sequence_max + 1]
    return sequence_of_numbers_with_at_most_3values


def get_sequence_with_same_modulus(list_of_complex_numbers):
    """
    Given a list of complex numbers, the function returns the largest sequence of numbers with the same modulus.
    :param list_of_complex_numbers: Its a list of dictionaries, which contains integer values.
    :return: It returns a list that contains the sequence with the most numbers with the same modulus.
    """
    start_of_sequence = 0
    length = 1
    end_of_sequence = 0
    max_length = 0
    modulus_looking_for = calculate_modulus(list_of_complex_numbers[0])
    for index in range(1, len(list_of_complex_numbers)):
        if modulus_looking_for == calculate_modulus(list_of_complex_numbers[index]):
            length += 1
            if length > max_length:
                start_for_largest_sequence = start_of_sequence
                end_of_sequence = index + 1
                max_length = length
        else:
            modulus_looking_for = calculate_modulus(list_of_complex_numbers[index])
            start_of_sequence = index
            length = 1
    return list_of_complex_numbers[start_for_largest_sequence:end_of_sequence]


# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

run_menu()
