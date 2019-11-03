def func1(a, b):
    """
    Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains
    only the elements that are common between the lists
    (without duplicates).
    """
    c = []
    for i in a:
        for k in b:
            if i == k and i not in c:
                c.append(i)
    return c


def func2(given_string):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    count = 0
    for i in given_string:
        if i == 'a':
            count += 1
    return count


def func3(given_int):
    """
    Write a Python program to check if a given positive integer is a power of three
    """
    while given_int % 3 == 0:
        given_int /= 3
    return given_int == 1


def func4(given_int):
    """
    adds the digits of a positive
    integer repeatedly until the
    result has a single digit
    """
    while len(str(given_int)) > 1:
        c = []
        for i in str(given_int):
            c.append(int(i))
        given_int = sum(c)
    return given_int


def func5(given_list):
    """
    pushes all zeros to the end of a list.
    """
    count = 0
    for i in given_list:
        if i == 0:
            given_list.remove(i)
            count += 1
    for i in range(count):
        given_list.append(0)
    return given_list


def func6(my_list):
    """
    checks a sequence of numbers is
    an arithmetic progression or not
    """
    difference = my_list[1] - my_list[0]
    for i in range(len(my_list) - 1):
        if not (my_list[i + 1] - my_list[i] == difference):
            return False
    return True


def func7(my_list):
    """
    finds the number in a list
    that doesn't occur twice.
    """
    result = []
    for i in my_list:
        if my_list.count(i) == 1:
            result.append(i)
    return result


def func8(my_list):
    """
    finds a missing number from a list
    """
    length = len(my_list)
    full_sum = (length + 1) * (length + 2) / 2
    my_list_sum = sum(my_list)
    return full_sum - my_list_sum


def func9(my_list):
    """
    counts the elements in a list
    until an element is a tuple.
    """
    count = 0
    for i in range(len(my_list) - 1):
        count += 1
        if type(my_list[i]) == tuple:
            return count - 1


def func10(my_string):
    """
    Write a program that will take the str parameter
    being passed and return the string in reversed order.
    """
    res = ''
    for i in my_string:
        res = i + res
    return res


def func11(my_int):
    """
    takes the num parameter being passed
    and returns the number of hours and minutes
    the parameter converts to (ie. if num = 63
    then the output should be 1:3)
    """
    hours = my_int // 60
    mins = my_int % 60
    return str(hours) + ':' + str(mins)


def func12(my_str):
    """
    takes the parameter being passed and returns
    the largest word in the string. If there are
    two or more words that are the same length,
    returns the first word from the string with
    that length. It ignores punctuation.
    """
    import string
    punct = set(string.punctuation)
    new_str = ''.join(x for x in my_str if x not in punct)
    longest_word = ''
    my_list = new_str.split(' ')
    for i in my_list:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word


def func13():
    """
    asks the user for a long string containing multiple words and
    prints back to the user the same string, except with the words
    in backwards order.
    """
    my_str = input('You can input your sentence here: \n')
    new_lst = my_str.split()
    return ' '.join(reversed(new_lst))


def func14():
    """
    asks the user how many Fibonnaci numbers
    to generate and then generates them
    """
    num = int(input("How many Fibonacci numbers to generate? "))
    result = []
    a = 1
    b = 1
    while a < num:
        result.append(a)
        tmp_var = b
        b = b + a
        a = tmp_var
    return result


def func15(my_list):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write
    one line of Python that takes this list a and makes
    a new list that has only the even elements of this
    list in it.
    """

    return [i for i in my_list if i % 2 == 0]


def func16(my_int):
    """
    adds up all the numbers from 1 to input number.
    For example: if the input is 4 then your program
    should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    res = 0
    for i in range(my_int + 1):
        res += i
    return res


def func17(my_int):
    """
    takes the parameter being passed
    and returns the factorial of it
    """
    res = 1
    for i in range(1, my_int + 1):
        res *= i
    return res


def func18(my_str):
    """
    take the str parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the alphabet
    (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
    (a, e, i, o, u) and finally return this modified string.
    """
    new_str = ''
    for i in my_str:
        if i == 'z':
            new_str += 'a'
            continue
        new_str += chr(ord(i) + 1)
    new_list = list(new_str)
    for i in range(len(new_str)):
        if new_str[i] in 'aeiou':
            new_list[i] = new_list[i].capitalize()
    return ''.join(new_list)


def func19(my_str):
    """
    Write a program that will take the str string parameter being passed and return
    the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    """
    my_list = sorted(list(my_str))
    return ''.join(my_list)


def func20(num1, num2):
    """
    Write a program that will take both parameters being passed and return the true if num2
    is greater than num1, otherwise return the false. If the parameter values are equal to
    each other then return the string -1
    """
    if num2 > num1:
        return True
    elif num1 == num2:
        return '-1'
    return False
