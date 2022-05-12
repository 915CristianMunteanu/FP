"""
  Write non-UI functions below
"""
import datetime


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
    return transaction['amount_of_money']


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
    assert process_given_command('   add 12 in descriere') == ('add', ['12', 'in', 'descriere'])
    assert process_given_command('insErt 25 12 out pacanele') == ('insert', ['25', '12', 'out', 'pacanele'])


def add_transaction_run(bank_account_transactions, command_parameters):
    """
    This function adds a new transaction on today date, with the details from command_parameters
    :param bank_account_transactions:Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters:Its a list of details as follows: First element is amount_of_money
                                                                Second element is type
                                                                Third elemnt is description
    :return:The function doesnt return anything, just appends one more element to the list of dictionaries bank_account_transactions.
    """
    curent_time = datetime.datetime.now()
    if len(command_parameters) != 3:
        raise ValueError("The given parameters are not valid!")
    else:
        command_parameters.insert(0, curent_time.day)
        insert_transaction_run(bank_account_transactions, command_parameters)


def insert_transaction_run(bank_account_transactions, command_parameters):
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


def remove_transactions_run(bank_account_transactions, command_parameters):
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
            going_through_the_list = 0
            while going_through_the_list < number_of_transactions:
                if get_transaction_type(bank_account_transactions[going_through_the_list]) == command_parameters[0]: #command_parameters[0] is the given type that we are searching for
                    del bank_account_transactions[going_through_the_list]
                    number_of_transactions -= 1
                    going_through_the_list -= 1
                going_through_the_list += 1

        else:
            number_of_transactions = int(len(bank_account_transactions))
            going_through_the_list = 0
            while going_through_the_list < number_of_transactions:
                if get_transaction_day(bank_account_transactions[going_through_the_list]) == int(command_parameters[0]): #command_parameters[0] is the given day that we are looking for
                    del bank_account_transactions[going_through_the_list]
                    number_of_transactions -= 1
                    going_through_the_list -= 1
                going_through_the_list += 1

    if len(command_parameters) == 3:
        number_of_transactions = int(len(bank_account_transactions))
        going_through_the_list = 0
        while going_through_the_list < number_of_transactions:
            if get_transaction_day(bank_account_transactions[going_through_the_list]) >= int(
                    command_parameters[0]) and get_transaction_day(
                    bank_account_transactions[going_through_the_list]) <= int(command_parameters[2]): #command_parameters[0] is the given first day that we need to compare the day of transactions
                del bank_account_transactions[going_through_the_list]                                 #command_parameters[0] is the given last day that we need to compare the day of transactions
                number_of_transactions -= 1
                going_through_the_list -= 1
            going_through_the_list += 1


def replace_transactions_run(bank_account_transactions, command_parameters):
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
    for going_through_the_list in range(len(bank_account_transactions)):
        if get_transaction_day(bank_account_transactions[going_through_the_list]) == int(
                command_parameters[0]) and get_transaction_type(                            #command_parameters[0] is the day of the transaction that we need to replace
            bank_account_transactions[going_through_the_list]) == command_parameters[       #command_parameters[1] is the type of the transaction that we need to replace
            1] and get_transaction_description(                                             #command_parameters[2] is the description of the transaction that we need to replace
            bank_account_transactions[going_through_the_list]) == command_parameters[2]:    #command_parameters[-1] is the amount_of_money that we need to put in the transaction
            bank_account_transactions[going_through_the_list]['amount_of_money'] = int(command_parameters[-1])
    return bank_account_transactions

    """
      Write the command-driven UI below
    """


def print_transaction_ui(transaction):
    """
    This function is used to print a transaction
    :param transaction: Its a dictionary
    :return:
    """
    print("Transaction: " + ' Day: ' +
          str(get_transaction_day(transaction)) + ' Amount of money:' +
          str(get_transaction_amount_of_money(transaction)) + ' Type:' +
          get_transaction_type(transaction) + ' Description: ' +
          get_transaction_description(transaction))


def list_transactions_run(bank_account_transactions, command_parameters):
    """
    This function is used for all the cases when needed to list something.
    We have more cases: 1. The list command_parameters has 1 element. In that case, we need to show all transactions of that type.
                        2. The list command_parameters has 2 elements. Then, we check if the first element is one of > < or =. If yes, we need to show all transactions that has the amount_of_money greater, smaller, or equal to the second parameter, depending on the first parameter.
                        If its not one of the > < or = then we need to calculate the balance, depending on the day which is the second parameter. Then, for each transaction that has a good day, we check the type. If its an in, we add, if its an out, we substract.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return:
    """
    if command_parameters == None:
        if len(bank_account_transactions) == 0:
            print("There are not any transactions!")
        for going_through_the_list in range(len(bank_account_transactions)):
            print_transaction_ui(bank_account_transactions[going_through_the_list])
    elif len(command_parameters) == 1:
        for going_through_the_list in range(len(bank_account_transactions)):
            if get_transaction_type(bank_account_transactions[going_through_the_list]) == command_parameters[0]:
                print_transaction_ui(bank_account_transactions[going_through_the_list])
    elif len(command_parameters) == 2:
        if command_parameters[0] == '=':
            for going_through_the_list in range(len(bank_account_transactions)):
                if get_transaction_amount_of_money((bank_account_transactions[going_through_the_list])) == int(
                        command_parameters[1]):
                    print_transaction_ui(bank_account_transactions[going_through_the_list])
        elif command_parameters[0] == '>':
            for going_through_the_list in range(len(bank_account_transactions)):
                if get_transaction_amount_of_money(bank_account_transactions[going_through_the_list]) > int(
                        command_parameters[1]):
                    print_transaction_ui(bank_account_transactions[going_through_the_list])
        elif command_parameters[0] == '<':
            for going_through_the_list in range(len(bank_account_transactions)):
                if get_transaction_amount_of_money(bank_account_transactions[going_through_the_list]) < int(
                        command_parameters[1]):
                    print_transaction_ui(bank_account_transactions[going_through_the_list])
        else:
            balance = 0
            for going_through_the_list in range(len(bank_account_transactions)):
                if get_transaction_day(bank_account_transactions[going_through_the_list]) <= int(command_parameters[1]):
                    if get_transaction_type(bank_account_transactions[going_through_the_list]) == 'in':
                        balance = balance + get_transaction_amount_of_money(
                            bank_account_transactions[going_through_the_list])
                    else:
                        balance = balance - get_transaction_amount_of_money(
                            bank_account_transactions[going_through_the_list])

            print("The balance until day " + str(command_parameters[1]) + ' is: ' + str(balance))


def run_command_ui():
    """
    This function is the main menu of the program. It initializes the bank_account_transactions with some values.
    There is created the dictionary with the commands.
    :return: The function doesnt do anything.
    """
    bank_account_transactions = [{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'}]
    command_options_dictionary = {'add': add_transaction_run, 'insert': insert_transaction_run,
                                  'list': list_transactions_run, 'remove': remove_transactions_run,
                                  'replace': replace_transactions_run}

    while True:
        print("Your options are: \n"
              "add <value> <type> <description> \n" +
              "insert <day> <value> <type> <description> \n" +
              "remove <day> \n" +
              "remove <start day> to <end day> \n" +
              "remove <type> \n" +
              "replace <day> <type> <description> with <value> \n" +
              "list \n" +
              "list <type> \n" +
              "list [ < | = | > ] <value> \n" +
              "list balance <day>")
        command_option = input("What do you want to do with the bank account? ")
        command_type, command_parameters = process_given_command(command_option)
        if command_type == 'exit':
            return
        else:
            command_options_dictionary[command_type](bank_account_transactions, command_parameters)


run_command_ui()