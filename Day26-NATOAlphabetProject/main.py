import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {data.letter: data.code for index, data in df.iterrows()}
print(data_dict)
is_loop_on = True
while is_loop_on:
    user_input = input("What is your name? ").upper()
    try:
        nato_list = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only alphabets are allowed!")
    else:
        print(nato_list)
        is_loop_on = False
