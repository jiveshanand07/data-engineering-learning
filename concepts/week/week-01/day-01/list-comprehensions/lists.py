'''
Docstring for concepts.week.week-01.day-01.lists
'''

'''
Lists comprehensions
'''

#Syntax
#[expression for item in iterable if condition]

'''
iterating through a list of numbers from 0-9 and returning the number in list if current iterating item is an even number
'''
events = [x for x in range(10) if x % 2 == 0]
print("events", events)


'''
assigning square of a number in iterable or each value
'''
squares = [x**2 for x in range(10)]
print("squares", squares)

words = ["rest", "red", "yellow"]
uppercase = [word.upper() for word in words]

print("Uppercase", uppercase)


'''
Your Tasks (write these):

1. List of squares from 1-20
2. All words from a list starting with 'a'
3. Convert list of strings to lowercase
4. Filter list to only numbers > 50
'''

# 1. List of squares from 1-20

square_numbers = [x**2 for x in range(1, 21)]
print("square_numbers", square_numbers)


# 2. All words from a list starting with 'a'
words_list = ['Apple', "Anthony", "John", "Jivesh", "Biran", "Claudia"]
words_starting_with_a = [word for word in words_list if word.lower().startswith('a')]

print("words_list", words_starting_with_a)


# 3. Convert list of strings to lowercase

words_list_to_uppercase = [word.upper() for word in words_list]
words_list_in_lowercase = [word.lower() for word in words_list_to_uppercase]

print("words in upper case", words_list_to_uppercase)
print("words in lower case", words_list_in_lowercase)


# 4. Filter list to only numbers > 50

filter_numbers_gt_50 = [num for num in range(1, 250) if num >50]
print("filter numbers wioth gt 50", filter_numbers_gt_50)

