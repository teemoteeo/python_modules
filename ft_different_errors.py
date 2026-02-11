#!/usr/bin/env python3
def garden_operations():
    temp_str = 'abc'
    temp_int = 25
    my_dict = {'a': 1, 'b': 2}
    print("Testing ValueError...")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        zero_division = temp_int / 0
    except ZeroDivisionError:
        print(f"Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open('non_existent_file.txt', 'r')
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        print(my_dict['c'])
    except KeyError:
        print(f"Caught KeyError: 'missing\_plant'\n")
    print("Testing multiple errors together...")
    try:
        temp = int(temp_str)
        zero_division = temp_int / 0
        open('non_existent_file.txt', 'r')
        print(my_dict['c'])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print(f"Caught an error, but program continues\n")

def test_garden_operations():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()

if __name__ == "__main__":
    test_garden_operations()
