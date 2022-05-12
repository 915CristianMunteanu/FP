"""
  Program functionalities module
"""
import datetime
import ui


def get_transaction_day(transaction):
    """
    This is a getter function, that given a transaction(dictionary) returns the day
    :param transaction: Dictionary of integer positive values and strings.
    :return: Returns the value of the day, which is a integer value between 1 and 30.
    """
    return transaction['day']


def get_transaction_amount_of_money(transaction):
    """
    This is a getter function, that given a transaction(dictionary) returns the amount_of_money of the transaction
    :param transaction: Dictionary of integer positive values and strings.
    :return: Returns the value of amount_of_money, which is a integer positive number
    """
    return int(transaction['amount_of_money'])


def get_transaction_type(transaction):
    """
    This is a getter function, that given a transaction(dictionary) returns the type of the transaction
    :param transaction: Dictionary of integer positive values and strings.
    :return: Returns the value of the type, which is a string, either in or out.
    """
    return transaction['type']


def get_transaction_description(transaction):
    """
    This is a getter function, that given a transaction(dictionary) returns the description of the transaction
    :param transaction: Dictionary of integer positive values and strings.
    :return: Returns the value of the description, which is a string.
    """
    return transaction['description']


def process_given_command(command_option):
    """
    This function is used to make the input of the user be processed by the program. Firstly, it strips the given string, to remove the whitespaces.
    Then, it does 1 split, to separate the command_type from the parameters.
    Then, if it has parameters, it splits them too.
    :param command_option: This is a string, containing the given command
    :return: The function returns 2 values:
                                            command_type-its the name of the command introduced
                                            command_parameters-a list of the command`s parameters
    """
    command_option = command_option.strip()
    list_of_command_elements = command_option.split(maxsplit=1)
    command_type = list_of_command_elements[0].lower() if len(list_of_command_elements) > 0 else None
    if len(list_of_command_elements) == 2:
        string_command_parameters = list_of_command_elements[1].lower()
        list_of_command_parameters = string_command_parameters.split()
    else:
        list_of_command_parameters = None
    return command_type, list_of_command_parameters


def test_process_given_command():
    """
    This is a test function to check if the process_given_command function works properly.
    :return:
    """
    assert process_given_command('add 10 out pizza') == ('add', ['10', 'out', 'pizza'])
    assert process_given_command('   add   12 in descriere') == ('add', ['12', 'in', 'descriere'])
    assert process_given_command('insErt 25 12 out pacanele') == ('insert', ['25', '12', 'out', 'pacanele'])
    assert process_given_command('remove   5') == ('remove', ['5'])


def add_transaction(bank_account_transactions, command_parameters):
    """
    This function adds a new transaction on today date, with the details from command_parameters
    :param bank_account_transactions:Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters:Its a list of details as follows: First element is amount_of_money
                                                                Second element is type
                                                                Third element is description
    :return:The function doesnt return anything, just appends one more element to the list of dictionaries bank_account_transactions.
    """
    curent_time = datetime.datetime.now()
    if len(command_parameters) != 3:
        raise ValueError("The given parameters are not valid!")
    else:
        command_parameters.insert(0, curent_time.day)
        insert_transaction(bank_account_transactions, command_parameters)


def insert_transaction(bank_account_transactions, command_parameters):
    """
    This function adds a new transaction on a given date, with the details from command_parameters
    :param bank_account_transactions:Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters:Its a list of details as follows: First element is the day
                                                                Second element is amount_of_money
                                                                Third element is type
                                                                Forth element is description
    :return:The function doesnt return anything, just appends one more element to the list of dictionaries bank_account_transactions.
    """
    if len(command_parameters) != 4:
        raise ValueError("The given parameters are not valid!")
    else:
        bank_account_transactions.append(
            {'day': int(command_parameters[0]), 'amount_of_money': int(command_parameters[1]),
             'type': command_parameters[2], 'description': command_parameters[3]})


def remove_transactions(bank_account_transactions, command_parameters):
    """
    This function removes transaction from the list bank_account_transactions.
    It has 3 cases: 1. The list command_parameters has 1 element and its the value 'in' or 'out', being the type.
                    2. The list command_parameters has 1 element and its and integer value, being the day.
                    3 The list command_parameters has 3 element , first being the first day of the transactions to be removed, the third being the last day of the transactions to be removed. The second element is useless, being 'to'
        :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
        :param command_parameters: Its a list of parameters, that can differ as explained upper.
        :return: Returns the modified new_bank_account_transactions, without the transactions that needed to be removed
        """
    if len(command_parameters) == 1:
        if command_parameters[0] == 'in' or command_parameters[0] == 'out':
            number_of_transactions = int(len(bank_account_transactions))
            current_element_index = 0
            while current_element_index < number_of_transactions:
                if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[
                    0]:  # command_parameters[0] is the given type that we are searching for
                    del bank_account_transactions[current_element_index]
                    number_of_transactions -= 1
                    current_element_index -= 1
                current_element_index += 1
        else:
            number_of_transactions = int(len(bank_account_transactions))
            current_element_index = 0
            while current_element_index < number_of_transactions:
                if get_transaction_day(bank_account_transactions[current_element_index]) == int(
                        command_parameters[0]):  # command_parameters[0] is the given day that we are looking for
                    del bank_account_transactions[current_element_index]
                    number_of_transactions -= 1
                    current_element_index -= 1
                current_element_index += 1
    if len(command_parameters) == 3:
        number_of_transactions = int(len(bank_account_transactions))
        current_element_index = 0
        while current_element_index < number_of_transactions:
            if get_transaction_day(bank_account_transactions[current_element_index]) >= int(
                    command_parameters[0]) and get_transaction_day(
                bank_account_transactions[current_element_index]) <= int(command_parameters[
                                                                             2]):  # command_parameters[0] is the given first day that we need to compare the day of transactions
                del bank_account_transactions[
                    current_element_index]  # command_parameters[0] is the given last day that we need to compare the day of transactions
                number_of_transactions -= 1
                current_element_index -= 1
            current_element_index += 1


def test_remove_transactions():
    """
    This is a function test for the function remove_transaction
    :return:
    """
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'}]
    remove_transactions(bank_account_transactions, ['in'])


test_remove_transactions()


def replace_transactions(bank_account_transactions, command_parameters):
    """
    This function is used to change some values in the already existing transaction. It looks for the values and only if it finds the exact same values it changes it. If not, the function doesnt do anything.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: Its a list of parameters as follows: 1st is the day that we are looking for
                                                                  2nd is the type that we are looking for
                                                                  3rd is the description that we are looking for
                                                                  4th is the word with, that is useless
                                                                  5th is the value that needs to be replaced.
    :return:
    """
    for current_element_index in range(len(bank_account_transactions)):
        if get_transaction_day(bank_account_transactions[current_element_index]) == int(
                command_parameters[0]) and get_transaction_type(
            # command_parameters[0] is the day of the transaction that we need to replace
            bank_account_transactions[current_element_index]) == command_parameters[
            # command_parameters[1] is the type of the transaction that we need to replace
            1] and get_transaction_description(
            # command_parameters[2] is the description of the transaction that we need to replace
            bank_account_transactions[current_element_index]) == command_parameters[
            2]:  # command_parameters[-1] is the amount_of_money that we need to put in the transaction
            bank_account_transactions[current_element_index]['amount_of_money'] = int(command_parameters[-1])
    return bank_account_transactions


def test_replace_transactions():
    """
    Function test for the function replace_transaction_run
    :return:
    """
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'}]
    replace_transactions(bank_account_transactions, ['12', 'in', 'salary', 'with', '2000'])
    assert bank_account_transactions == [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                         {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                         {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                         {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                         {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                         {'day': 12, 'amount_of_money': 2000, 'type': 'in', 'description': 'salary'}]
    bank_account_transactions = [{'day': 13, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'something'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'}]
    replace_transactions(bank_account_transactions, ['6', 'out', 'something', 'with', '17'])
    assert bank_account_transactions == [{'day': 13, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                         {'day': 1, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                         {'day': 6, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                         {'day': 6, 'amount_of_money': 17, 'type': 'out', 'description': 'something'},
                                         {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                         {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'}]


test_replace_transactions()


def list_transaction_with_1_parameter(bank_account_transactions, command_parameters):
    """
    This function is used to list the transactions when the command_parameters has 1 or 0 parameters.
    If it has 2 parameters a new function is accessed.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return:
    """
    if command_parameters == None:
        if len(bank_account_transactions) == 0:
            raise ValueError("There are not any transactions! ")
        for current_element_index in range(len(bank_account_transactions)):
            ui.print_transaction_ui(bank_account_transactions[current_element_index])
    elif len(command_parameters) == 1:
        for current_element_index in range(len(bank_account_transactions)):
            if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[0]:
                ui.print_transaction_ui(bank_account_transactions[current_element_index])
    elif len(command_parameters) == 2:
        list_transactions_with_2_parameters_given(bank_account_transactions, command_parameters)


def list_transactions_with_2_parameters_given(bank_account_transactions, command_parameters):
    """
    This function is used to list transactions when the list command_parameters has 2 elements.
    We have more cases. 1. The first parameter is one of = ,< ,>.
                        2. The first parameter is a number, which is the day to which we need to calculate the balance.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return:
    """
    if command_parameters[0] == '=':
        for current_element_index in range(len(bank_account_transactions)):
            if get_transaction_amount_of_money((bank_account_transactions[current_element_index])) == int(
                    command_parameters[1]):
                ui.print_transaction_ui(bank_account_transactions[current_element_index])
    elif command_parameters[0] == '>':
        for current_element_index in range(len(bank_account_transactions)):
            if get_transaction_amount_of_money(bank_account_transactions[current_element_index]) > int(
                    command_parameters[1]):
                ui.print_transaction_ui(bank_account_transactions[current_element_index])
    elif command_parameters[0] == '<':
        for current_element_index in range(len(bank_account_transactions)):
            if get_transaction_amount_of_money(bank_account_transactions[current_element_index]) < int(
                    command_parameters[1]):
                ui.print_transaction_ui(bank_account_transactions[current_element_index])


def calculate_sum_of_transactions(bank_account_transactions, command_parameters):
    """
    This function calculates the sum of amount_of_money that have the type given by command_parameters.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return: It returns a integer value, which is the sum.
    """
    sum_of_amount_of_money = 0
    if command_parameters == None:
        raise ValueError("Not enough parameters given!")
    else:
        if command_parameters[0] == 'in' or command_parameters[0] == 'out':
            for current_element_index in range(len(bank_account_transactions)):
                if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[0]:
                    sum_of_amount_of_money += get_transaction_amount_of_money(bank_account_transactions[current_element_index])
    return sum_of_amount_of_money


def test_calculate_sum_of_transactions():
    """
    Test function for the function calculate_sum_of_transactions.
    :return:
    """
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 200, 'type': 'in', 'description': 'salary'}]
    assert calculate_sum_of_transactions(bank_account_transactions, ['in']) == 1000
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 200, 'type': 'in', 'description': 'salary'}]
    assert calculate_sum_of_transactions(bank_account_transactions, ['out']) == 1000




def find_max_value_in_given_day(bank_account_transactions, command_parameters):
    """
    This function goes through the list bank_account_transactions and is searching for values of amount_of_money greater than the already existing maximum_amount_of_money variable.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return: Returns a integer value, which is maximum_amount_of_money.
    """
    maximum_amount_of_money = 0
    if command_parameters == None or len(command_parameters) == 1:
        raise ValueError("Not enough parameters given!")
    else:
        if command_parameters[0] == 'in' or command_parameters[
            0] == 'out':  # command_parameters[0] is the type introduced in the command, which can be in our out
            for current_element_index in range(
                    len(bank_account_transactions)):  # command_parameters[1] is the day introduced in the command, which is a string that can be converted to a integer.
                if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[
                    0] and get_transaction_day(bank_account_transactions[current_element_index]) == int(
                    command_parameters[1]):
                    if get_transaction_amount_of_money(
                            bank_account_transactions[current_element_index]) > maximum_amount_of_money:
                        maximum_amount_of_money = get_transaction_amount_of_money(
                            bank_account_transactions[current_element_index])
    if maximum_amount_of_money == 0:
        raise ValueError("There are not any transactions of the given type in the given day.")
    else:
        return maximum_amount_of_money


def test_find_max_value_in_given_day():
    """
    This function is a test function for find_max_value_in_given_day.
    :return:
    """
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 200, 'type': 'in', 'description': 'salary'}]
    assert find_max_value_in_given_day(bank_account_transactions, ['in', '12']) == 500
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'out', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'out', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 700, 'type': 'out', 'description': 'salary'}]
    assert find_max_value_in_given_day(bank_account_transactions, ['out', '12']) == 700


test_find_max_value_in_given_day()


def filter_transactions(bank_account_transactions, command_parameters):
    """
    This function its the brother of the function remove.
    :param bank_account_transactions:
    :param command_parameters:
    :return:
    """
    if command_parameters == None:
        raise ValueError("Not enough parameters given!")
    else:
        if len(command_parameters) == 1 and (command_parameters[0] == 'in' or command_parameters[0] == 'out'):
            new_bank_account_transactions = []
            for current_element_index in range(len(bank_account_transactions)):
                if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[0]:
                    new_bank_account_transactions.append(bank_account_transactions[current_element_index])
        elif len(command_parameters) == 2:
            new_bank_account_transactions = []
            for current_element_index in range(len(bank_account_transactions)):
                if get_transaction_type(bank_account_transactions[current_element_index]) == command_parameters[
                    0] and get_transaction_amount_of_money(bank_account_transactions[current_element_index]) < int(
                    command_parameters[1]):
                    new_bank_account_transactions.append(bank_account_transactions[current_element_index])

    bank_account_transactions[:]=new_bank_account_transactions[:]

