import pandas

nato_dataframe = pandas.read_csv("./NATO_Alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

word = input("Enter a word: ")
nato_word = [nato_dict[letter.upper()] for letter in word]
print(nato_word)
