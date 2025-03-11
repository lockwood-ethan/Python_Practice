import pandas

nato_dataframe = pandas.read_csv("./NATO_Alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        nato_word = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()