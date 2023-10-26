from itertools import permutations

def gen_sen(input_string):
    words = input_string.split()

    word_perm = permutations(words)

    for permutation in word_perm:
        sentence = ' '.join(permutation)
        print(sentence)

input_string = input("Enter a sentence: ")

print("All possible sentences:")
gen_sen(input_string)