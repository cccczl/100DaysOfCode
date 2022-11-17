# NATO Alphabet

import pandas as pd

CSV_FILE = "nato_phonetic_alphabet.csv"


def get_input():
    """Gets input from the user, turns it into uppercase and returns it as STR."""
    while True:
        text = input("> ").upper()
        if text == "":
            print("Please enter a word.")
        else:
            return text


# create a data frame from the csv file
codes_df = pd.read_csv(CSV_FILE)

# create a dictionary using a dictionary comprehension
codes_dict = {row.letter: row.code for (index, row) in codes_df.iterrows()}

while True:
    print("Enter a word to convert or type \"!quit\" to quit:")
    word = get_input()
    # this way it's still possible to covert the word "quit"
    if word == "!QUIT":
        break

    if output := [codes_dict[char] for char in word if char in codes_dict]:
        print(" ".join(output))

print("Goodbye.")
