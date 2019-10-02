from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for i in data:
        if 'name' in i.keys():
            i['name'] = i['name'].capitalize()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for i in data:
        for k in redundant_keys:
           i.pop(k)
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    new_dict = []
    for i in data:
        if value in i.values():
            new_dict.append(i)
    return new_dict


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    min_value = None
    for value in data:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """
    if data:
        new_lst = []
        for i in data:
            i = str(i)
            new_lst.append(i)
        new_lst.sort(key=len)
        shortest = new_lst[0]
        return shortest


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    min_value = data[0]
    for i in data:
        if key in i.keys():
            if i[key] < min_value[key]:
                min_value = i
    return min_value


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    result = []
    for i in data:
        result.extend(i)
    return max(result)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    if len(data) > 0:
        return sum(data)
    else:
        return 0


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum(map(ord, text))


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    value = 2
    while value <= 201:
        for i in range(2, value):
            if value % i == 0:
                value += 1
                break
        else:
            yield value
            value += 1
