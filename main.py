import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}


def nato():
    try:
        phonetic_word = input("Enter a word:").upper()
        phonetic_list = [phonetic_alphabets[letter] for letter in phonetic_word]
        print(phonetic_list)
    except KeyError:
        print("sorry only alphabets allowed")
    finally:
        nato()


nato()
