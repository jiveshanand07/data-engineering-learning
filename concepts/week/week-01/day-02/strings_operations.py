'''
Docstring for concepts.week.week-01.day-02.strings_operations
'''

'''
String Operations
'''

s = "Hello World!"

#slicing

s[:5]
print("Slice 1:", s[:5])
print("slice 2:", s[6:])
print("Reversing a string: ", s[::-1])
print("Every Second Character: ", s[::2])

print("lower case", s.lower())
print("Upper Case", s.upper())

print("Stripping which whill remove white spaces", s.strip())
print("split into list", s.split())
print("Splitying a string", '   '.join(s.split()))


print("isAlphaNum", s.isalnum())
print("isDigit: ", s.isdigit())


#Practice

'''
write a function to reverse a string
'''

def reverse_string(value: str):
    return value[::-1]

print("reverse a string", reverse_string("Hellloo"))

'''
Write a function to check if string is palindrome (use slicing!)
'''

def is_palindrome(value: str) -> bool:
    return value == value[::-1]


'''
Write a function to reverse words in a sentence
'''

def reverse_words_in_sentence(s: str) -> str:
    words: list = s.split()
    return ' '.join(words[::-1])

print("reverse a sentence:", reverse_words_in_sentence("hello world") )