import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

split_words = words.split()

word_cache = {}
starting_word = []
stopped_word = []

# TODO: analyze which words can follow other words


def word_bank():
    for index, word in enumerate(split_words):
        if index < len(split_words) - 1:
            if funcStarted(word):
                starting_word.append(word)
            if funcStopped(word):
                stopped_word.append(word)
            if word not in word_cache:
                word_cache[word] = []
            word_cache[word].append(split_words[index + 1])


def funcStarted(word):
    if word[0].isupper():
        return True
    elif word[0] == '"' and word[1].isupper():
        return True
    else:
        return False


def funcStopped(word):
    if word.endswith(("!", "?", ".")):
        return True
    elif words.endswith('"') and word[:-1].word.endswith(("!", "?", ".")):
        return True
    else:
        return False


# TODO: construct 5 random sentences
word_bank()
for i in range(5):
    print(f"sentence #{i + 1}:")
    word = random.choice(starting_word)
    print(word, end=" ")
    while not funcStopped(word):
        word = random.choice(word_cache[word])
        print(word, end=" ")
    print("\n")
