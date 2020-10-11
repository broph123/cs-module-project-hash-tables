
def word_count(s):

    # Your code here
    counts = {}
    newWords = []

    split = s.lower().split()
    print(split)

    for word in split:
        newWords.append(word.replace(':', '').replace(';', '').replace(',', '').replace('.', '').replace('-', '').replace('+', '').replace('=', '').replace('/', '').replace('|', '').replace(
            '[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('*', '').replace('^', '').replace('&', '').replace('"', '').replace('\\', ''))

    if newWords == [""]:
        return counts

    for words in newWords:
        counts[words] = newWords.count(words)

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
