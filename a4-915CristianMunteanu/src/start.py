"""
  Start the program by running this module
"""
import functions
import ui

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
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 200, 'type': 'in', 'description': 'salary'}]
    command_options_dictionary = {'add': functions.add_transaction, 'insert': functions.insert_transaction,
                                  'list': functions.list_transaction_with_1_parameter, 'remove': functions.remove_transactions,
                                  'replace': functions.replace_transactions,'sum':ui.calculate_sum_of_transactions_ui,'max':ui.find_max_value_in_given_day_ui,
                                  'filter':functions.filter_transactions}
    list_of_bank_account_transactions=[[{'day': 20, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 1, 'amount_of_money': 300, 'type': 'out', 'description': 'pizza'},
                                 {'day': 5, 'amount_of_money': 500, 'type': 'out', 'description': 'pizza'},
                                 {'day': 6, 'amount_of_money': 200, 'type': 'out', 'description': 'pizza'},
                                 {'day': 7, 'amount_of_money': 100, 'type': 'in', 'description': 'pizza'},
                                 {'day': 12, 'amount_of_money': 100, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 500, 'type': 'in', 'description': 'salary'},
                                 {'day': 12, 'amount_of_money': 200, 'type': 'in', 'description': 'salary'}]]
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
              "list balance <day>"+
              "sum <type> \n"+
              "max <type> <day> \n"+
              "filter <type> \n"+
              "filter <type> <value> \n")
        command_option = input("What do you want to do with the bank account? ")
        command_type, command_parameters = functions.process_given_command(command_option)
        if command_type == 'exit':
            return
        else:
            try:
                if command_type == 'undo' and len(list_of_bank_account_transactions) > 1:
                    del list_of_bank_account_transactions[-1]
                    bank_account_transactions[:] = list_of_bank_account_transactions[:][-1]
                else:
                    if command_type == 'undo':
                        print("Cant go further back")
                if command_type == 'list' and command_parameters != None:
                    if command_parameters[0] == 'balance':
                            ui.list_balance(bank_account_transactions,command_parameters)
                    else:
                        command_options_dictionary[command_type](bank_account_transactions, command_parameters)
                elif command_type != 'undo' and command_type != 'list':
                    command_options_dictionary[command_type](bank_account_transactions, command_parameters)
                    list_of_bank_account_transactions.append([])
                    list_of_bank_account_transactions[-1][:]=bank_account_transactions[:]
                elif command_type == 'list':
                    command_options_dictionary[command_type](bank_account_transactions, command_parameters)
            except ValueError as ve:
                print(ve)



run_command_ui()