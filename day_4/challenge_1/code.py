"""Solution to Day 4 Challenge 1 for Advent of Code 2020."""

from typing import List


def process_passport(passport_fields: List[str]) -> bool:
    """
    Processes data for a single passport to see if it has all required fields.

    Args:
        passport_fields (List[str]): List of field data in the format
            "name:value".

    Returns:
        bool: True if all required fields are present, False otherwise.
    """
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    # check that each field is contained in the list of this passport's fields
    # also check that each field actually has a value (field + ':' = length 4)
    for field in passport_fields:
        current_field = field[:3]
        if current_field in required_fields and len(field) > 4:
            required_fields.remove(current_field)

    return len(required_fields) == 0


def count_valid_passports(lines: List[str]) -> int:
    """
    Count the number of valid passports.
    Each passport consists of one or more sequential strings from the list.
    Each passport is separated by an empty string.

    Args:
        lines (List[str]): A list of strings containing passport information.

    Returns:
        int: The number of valid passports.
    """
    valid_passport_count = 0
    passport_fields = []

    for line in lines:
        [passport_fields.append(item) for item in line.split()]
        if line == "" or line == lines[-1]:
            if process_passport(passport_fields):
                valid_passport_count += 1
            passport_fields = []

    return valid_passport_count


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        input_data = [line.rstrip() for line in input_file]
    solution = count_valid_passports(input_data)
    print(solution)
