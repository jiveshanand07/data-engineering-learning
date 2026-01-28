'''
Docstring for concepts.week.week-01.day-01.disctionaries-essentials.dictionaries
'''


'''
Dictionary Essentials
'''

# critical methods

default = "default"
d = {} # empty dictionary

print("dictionary 01", d)
d.setdefault("key", "Hello")
print("dictionary 02", d)
d.get('key', default) # Always use this instead of d[key]
print("dictionary 03", d.get('key', default))
d.setdefault('key', default) # get or create
print("dictionary 04", d)
d['key'] = 20
print("dictionary 05", d)

d['key'] = d.get('key', 0) +1
print("dictionary 06", d)


#character frequency

freq = {}

for char in "hello":
    freq[char] = freq.get(char, 0) + 1

print('frequency', freq)




# Your Task:
# Write a function that counts word frequency in a sentence

def count_word_freq(sentence: str):
    print("sentence.split(' ')", sentence.split(' '))
    freq = {}
    for word in sentence.split(' '):
        freq[word] = freq.get(word, 0) + 1

    return freq

print("count frequerncy of words in a sentence", count_word_freq("Hello Dear! How are you doing..? Did you get a chance to check on someone else in the office?"))