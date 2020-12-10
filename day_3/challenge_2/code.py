"""Solution to Day 3 Challenge 2 for Advent of Code 2020."""

from typing import List


def get_next_location(grid_height: int, grid_width: int, cur_x: int, cur_y: int, delta_x: int, delta_y: int) -> (int, int):
    """
    Gets the next location in an axis grid space that loops horizontally.

    Args:
        grid_height (int): The height before the space loops.
        grid_width (int): The width before the space loops.
        cur_x (int): The current x position.
        cur_y (int): The current y position.
        delta_x (int): The amount to shift right for the next position.
        delta_y (int): The amount to shift down for the next position.

    Returns:
        Tuple (int, int): The new x and y coordinates in the grid.
    """
    return (cur_x + delta_x) % grid_width, (cur_y + delta_y)


def get_tree_hits(input_grid: List[str], right: int, down: int) -> int:
    """
    Get the number of trees encountered via a line through the grid.

    Args:
        input_grid (List[str]): '.' represents a free space while '#'
            represents a tree.
        right (int): The amount right to check for the next tree.
        down (int): The amount down to check for the next tree.

    Returns:
        int: The number of trees encountered.
    """
    grid_height = len(input_grid)
    grid_width = len(input_grid[0])
    num_trees = 0
    loc_x = loc_y = 0
    while loc_y < grid_height:
        if input_grid[loc_y][loc_x] == '#':
            num_trees += 1
        loc_x, loc_y = get_next_location(
            grid_height, grid_width, loc_x, loc_y, right, down)

    return num_trees


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        input_grid = [line.rstrip() for line in input_file]
    solution = (
        get_tree_hits(input_grid, 1, 1) *
        get_tree_hits(input_grid, 3, 1) *
        get_tree_hits(input_grid, 5, 1) *
        get_tree_hits(input_grid, 7, 1) *
        get_tree_hits(input_grid, 1, 2)
    )
    print(solution)
