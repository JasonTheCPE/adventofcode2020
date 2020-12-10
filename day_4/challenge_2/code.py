"""Solution to Day 4 Challenge 2 for Advent of Code 2020."""

from typing import List
import re

VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
HEIGHT_REGEX = re.compile(r"^(?P<value>\d+)(?P<unit>\w\w)$")
HAIR_REGEX = re.compile(r"^#(\d|[a-f]){6}$")
PASSPORT_REGEX = re.compile(r"^\d{9}$")


def validate_height(height_str: str) -> bool:
    """
    Validates that heights have units and fall in a specified range.

    Args:
        height_str (str): The string value of the height field.

    Returns:
        bool: True if the height is valid, False otherwise.
    """
    results = HEIGHT_REGEX.search(height_str)
    value = results.group("value") if results else None
    unit = results.group("unit") if results else None
    if value and value.isdigit():
        value = int(value)
    else:
        return False

    if unit == "cm":
        return 150 <= value <= 193
    elif unit == "in":
        return 59 <= value <= 76

    return False


REQUIRED_FIELDS = {
    "byr": lambda x: 1920 <= int(x) <= 2002 if x.isdigit() else False,
    "iyr": lambda x: 2010 <= int(x) <= 2020 if x.isdigit() else False,
    "eyr": lambda x: 2020 <= int(x) <= 2030 if x.isdigit() else False,
    "hgt": validate_height,
    "hcl": HAIR_REGEX.match,
    "ecl": lambda x: x in VALID_EYE_COLORS,
    "pid": PASSPORT_REGEX.match
}


def process_passport(passport_fields: List[str]) -> bool:
    """
    Processes data for a single passport to see if it has all required fields.

    Args:
        passport_fields (List[str]): List of field data in the format
            "name:value".

    Returns:
        bool: True if all required fields are present and valid, False
            otherwise.
    """
    required_fields = REQUIRED_FIELDS.copy()

    # check that each field is contained in the list of this passport's fields
    # also check that each field is valid
    for field in passport_fields:
        field_list = field.split(':')
        if len(field_list) != 2:
            continue

        field_name = field_list[0]
        field_value = field_list[1]

        if field_name in required_fields:
            if required_fields[field_name](field_value):
                required_fields.pop(field_name)
            else:  # return false to prevent duplicate field checks
                return False

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
