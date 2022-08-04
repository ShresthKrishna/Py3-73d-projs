import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index,row) in data.iterrows():
#     print(row.code)
dictionary = {code.letter: code.code for (letter,code) in data.iterrows()}
def gen_phonetic():
    word = input("Enter any word: ").upper()
        #if key ==  letters for letters in list(word)
    try:
        list1 = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        print(list1)
gen_phonetic()
