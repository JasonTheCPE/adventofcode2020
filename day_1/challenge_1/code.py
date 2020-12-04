"""Solution to Day 1 Challenge 1 for Advent of Code 2020."""

from typing import List, Optional


def find_twos_product(values: List[int], target_value: int = 2020) -> Optional[int]:
    """
    Find two numbers in a list that sum to a target value and returns their
    product.

    Args:
        values (List[int]): A list of integer values.
        target_value (int, optional): The target value. Defaults to 2020.

    Returns:
        int: The product of two numbers from the list that sum to the target.
    """
    value_set = set(values)

    for value in value_set:
        paired_value = target_value - value
        if paired_value in value_set:
            return value * paired_value


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        input_values = [int(line) for line in input_file]
    solution = find_twos_product(input_values)
    print(solution)
