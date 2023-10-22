from itertools import product

def generate_sentences(input_string):
    words = input_string.split()
    
    # Generate all possible combinations of words
    word_combinations = product(words, repeat=len(words))
    
    # Construct sentences and print them
    for combination in word_combinations:
        sentence = ' '.join(combination)
        print(sentence)