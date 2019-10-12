def func1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in a:
        for k in b:
            if i == k and i not in c:
                c.append(i)
    return c


def func2():
    given_string = 'I am a good developer. I am also a writer'
    count = 0
    for i in given_string:
        if i == 'a':
            count += 1
    return count


def func3(given_int):
    while given_int % 3 == 0:
        given_int /= 3
    return given_int == 1


def func4(given_int):
    while len(str(given_int)) > 1:
        c = []
        for i in str(given_int):
            c.append(int(i))
        # c = [int(i) for i in str(given_int)]
        given_int = sum(c)
    return given_int


def func5(given_list):
    count = 0
    for i in given_list:
        if i == 0:
            given_list.remove(i)
            count += 1
    for i in range(count):
        given_list.append(0)
    return given_list


def func6(my_list):
    difference = my_list[1] - my_list[0]
    for i in range(len(my_list) - 1):
        if not (my_list[i + 1] - my_list[i] == difference):
            return False
    return True


def func7(my_list):
    result = 0
    for i in my_list:
        result ^= i
    return result


def func8(my_list):
    length = len(my_list)
    full_sum = (length + 1) * (length + 2) / 2
    my_list_sum = sum(my_list)
    return full_sum - my_list_sum


def func9(my_list):
    count = 0
    for i in range(len(my_list) - 1):
        count += 1
        if type(my_list[i]) == tuple:
            return count - 1


def func10(my_string):
    res = ''
    for i in my_string:
        res = i + res
    return res


def func11(my_int):
    hours = round(my_int / 60)
    mins = my_int % 60
    return str(hours) + ':' + str(mins)


def func12(my_str):
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
    my_str = input('You can input your sentence here: \n')
    new_lst = my_str.split()
    return ' '.join(reversed(new_lst))


def func14():
    num = int(input("How many Fibonacci numbers to generate? "))
    result = []
    a, b = 1
    while a < num:
        result.append(a)
        tmp_var = b
        b = b + a
        a = tmp_var
    return result


def func15(my_list):
    # c = []
    return [i for i in my_list if i % 2 == 0]
    # for i in my_list:
    # if i % 2 == 0:
    #  c.append(i)
    # return c


def func16(my_int):
    res = 0
    for i in range(my_int + 1):
        res += i
    return res


def func17(my_int):
    res = 1
    for i in range(1, my_int + 1):
        res *= i
    return res


def func18(my_str):
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
    my_list = sorted(list(my_str))
    return ''.join(my_list)


def func20(num1, num2):
    if num2 > num1:
        return True
    elif num1 == num2:
        return '-1'
    return False
