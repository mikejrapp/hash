
import re
import time


def main():
    display_instructions()
    user_input = get_user_input()

    while user_input is not False:
        handle_user_input(user_input)
        user_input = get_user_input()

    print("Shutting down...")
    time.sleep(3)


def display_instructions():
    welcome = "Welcome to the Hash Program!"
    instructions = "Please enter a word or sentence to be hashed"
    explain_test = "To see specific test cases please enter #test"

    print(welcome)
    print(instructions)
    print(explain_test)


def get_letter_map():
    letter_values = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        " ": 31
    }

    return letter_values


def get_user_input():
    prompt = "\nPlease enter the value you would like to hash (or type exit to quit): "
    quit_pattern = re.compile("[eE]xit|[qQ]uit")

    try:
        user_input = raw_input(prompt)

        if quit_pattern.search(user_input):
            return False
        else:
            return user_input
    except IOError:
        print("Input has failed. Shutting down.")
        time.sleep(3)
        exit(1)


def handle_user_input(user_input):

    if user_input.find("#test") > -1:
        display_test_cases()
    else:
        print(get_hash_value(user_input))


def get_hash_value(string):
    letter_map = get_letter_map()

    string = sanitize_string(string)

    hash_value = 0

    for letter in string:
        hash_value += letter_map.get(letter.lower())

    hash_value %= 31

    return hash_value


def sanitize_string(string):

    # find symbols that will break the hash but keep the spaces since that is part of the hash
    symbol_pattern = "[^\s\w]"
    # find numbers since those will break the hash as well
    number_pattern = "\d"

    # replace all symbols and numbers with blank
    string = re.sub(symbol_pattern, "", string)
    string = re.sub(number_pattern, "", string)

    return string


def display_test_cases():
    description = "Please see the table below. The string in the left column should match the value in the right column"
    test_case_table = {
        "| cat         |": "       24 |",
        "| Don't Panic |": "        3 |",
        "| book        |": "       12 |",
    }

    print(description)

    for string, hash_value in test_case_table.items():
        print(string + hash_value)


main()
