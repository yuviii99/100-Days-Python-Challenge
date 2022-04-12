import pandas


# Generate a list of NATO Phonetic Alphabets
df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {data.letter: data.code for index, data in df.iterrows()}
user_input = input("What is your name? ").upper()
nato_list = []
for alphabet in user_input:
    nato_list.append(data_dict[alphabet])
print(nato_list)
