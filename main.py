import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())
phonetic_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_alphabets)

phonetic_word = input("Enter a word:").upper()
phonetic_list = [phonetic_alphabets[letter] for letter in phonetic_word]
print(phonetic_list)
