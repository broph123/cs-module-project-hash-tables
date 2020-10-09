# import random


# word_cache = {}

# # Read in all the words in one go
# with open("input.txt") as f:
#     words = f.read()
#     # for word in words:
#     # print(word, end='')

# w = words.split()
# # print(w)


# # TODO: analyze which words can follow other words
# # Your code here
# for i, v in enumerate(w):
#     if i == len(w)-1:
#         continue

#     # print(w[i+1], v)
#     # word_cache[v] = keys.append(w[i+1])
#     word_cache.setdefault(v, []).append(w[i+1])

# print(word_cache)


# def start_word(word):
#     # return a word
#     if word is capital or ":
#         return True

#     return False


# def stop_word(x):
#     stopList = [`.?!`, `"`]
#     if x is in stopList:
#         return True

#      return False

#     # if x ends .?! or followed by ""
#     # end the sentence


# # TODO: construct 5 random sentences
# # Your code here
# for k in word_cache.keys:
