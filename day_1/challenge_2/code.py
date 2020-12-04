"""Solution to Day 1 Challenge 2 for Advent of Code 2020."""

from typing import List, Set, Optional

def find_twos_product(value_set: Set[int], target_value: int) -> int:
    """
    Find two numbers in a list that sum to a target value and returns their
    product.

    Args:
        values (List[int]): A list of integer values.
        target_value (int, optional): The target value.

    Returns:
        int: The product of two numbers from the list that sum to the target.
    """
    for value in value_set:
        paired_value = target_value - value
        if paired_value in value_set:
            return value * paired_value

def find_threes_product(values: List[int], target_value: int = 2020) -> int:
    """
    Find three numbers in a list that sum to a target value and returns their
    product.

    Args:
        values (List[int]): A list of integer values.
        target_value (int, optional): The target value. Defaults to 2020.

    Returns:
        int: The product of three numbers from the list that sum to the target.
    """
    value_set = set(values)

    for value in value_set:
        remainder = target_value - value
        twos_product = find_twos_product(value_set, remainder)
        if twos_product:
            return value * twos_product


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        input_values = [int(line) for line in input_file]
    solution = find_threes_product(input_values)
    print(solution)
