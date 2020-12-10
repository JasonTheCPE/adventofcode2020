"""Solution to Day 2 Challenge 1 for Advent of Code 2020."""

from typing import List
import re


def find_valid_passwords(values: List[str]) -> int:
    """
    Find the number of valid passwords in a list containing both the policy and
    the passwords.

    Args:
        values (List[str]): A list of password policy rules followed by a colon
        and the password to check.

    Returns:
        int: The number of valid passwords
    """
    search_reg = re.compile(
        r"\b(?P<first>[0-9]+)-(?P<second>[0-9]+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)")
    valid_password_count = 0

    for value in values:
        results = search_reg.search(value)
        target_char = results.group("letter")
        password = results.group("password")
        first_index = int(results.group("first")) - 1
        second_index = int(results.group("second")) - 1

        if (target_char == password[first_index]) != (target_char == password[second_index]):
            valid_password_count += 1

    return valid_password_count


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        input_values = [line for line in input_file]
    solution = find_valid_passwords(input_values)
    print(solution)
