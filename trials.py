"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for itm in items:
        print(itm)

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []
    for i in range(len(items)-1):
        if i % 2 != 0:
            result.append(items[i])
    return result 


def print_as_numbered_list(items):
    i = 1
    for itm in items:
        print(f"{i}. {itm}")

        i += 1


def get_range(start, stop):
    const_num = []

    for num in range(start , stop):
        const_num.append(num)
    return const_num


def censor_vowels(word):
    vowels = ["a","e","i","o","u",]
    chars = []
    for letter in word:
        if letter in vowels:
            chars.append("*")
        else:
            chars.append(letter)
    return chars



def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
