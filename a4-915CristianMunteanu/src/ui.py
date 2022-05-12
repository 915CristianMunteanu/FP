"""
  User interface module
"""
import functions


def print_transaction_ui(transaction):
    """
    This function is used to print a transaction
    :param transaction: Its a dictionary
    :return:
    """
    print("Transaction: " + ' Day: ' +
          str(functions.get_transaction_day(transaction)) + ' Amount of money:' +
          str(functions.get_transaction_amount_of_money(transaction)) + ' Type:' +
          functions.get_transaction_type(transaction) + ' Description: ' +
          functions.get_transaction_description(transaction))

def list_balance(bank_account_transactions,command_parameters):
    """
    This function is used to to handle the situation when its needed to calculate the balanca.
    It adds the in type transactions and subtract the out type transactions.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return:
    """
    balance = 0
    for current_element_index in range(len(bank_account_transactions)):
        if functions.get_transaction_day(bank_account_transactions[current_element_index]) <= int(command_parameters[1]):
            if functions.get_transaction_type(bank_account_transactions[current_element_index]) == 'in':
                balance = balance + functions.get_transaction_amount_of_money(
                    bank_account_transactions[current_element_index])
            else:
                balance = balance - functions.get_transaction_amount_of_money(
                    bank_account_transactions[current_element_index])
    print("The balance until day " + str(command_parameters[1]) + ' is: ' + str(balance))


def calculate_sum_of_transactions_ui(bank_account_transactions, command_parameters):
    """
    This is the UI function for the function calculate_sum_of_in_transactions.
    It prints the ValueErrors, or if not any, prints the sum.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return: Doesnt return anything, just prints.
    """
    try:
        print(functions.calculate_sum_of_transactions(bank_account_transactions, command_parameters))
    except ValueError as ve:
        print(ve)

def find_max_value_in_given_day_ui(bank_account_transactions, command_parameters):
    """
    This is the UI function for the function calculate_sum_of_in_transactions.
    It prints the ValueErrors, or if not any, prints the maximum_amount_of_money.
    :param bank_account_transactions: Its a list of dictionaries, which contains all the transactions from the bank account.
    :param command_parameters: List of strings.
    :return: Doesnt return anything, just prints
    """
    try:
        print(functions.find_max_value_in_given_day(bank_account_transactions, command_parameters))
    except ValueError as ve:
        print(ve)