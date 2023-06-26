#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists.

    args:
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns:
    a new list (length = list_length) with all divisions
    """

    new_list = list(range(list_length))
    for i in range(list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            new_list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            new_list[i] = 0
            print("division by 0")
        except IndexError:
            new_list[i] = 0
            print("out of range")
        finally:
            pass
    return new_list
