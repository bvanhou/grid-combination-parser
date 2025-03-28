"""
Given a 10x10 grid of integers, and the task is:
- How many different combinations are there of three adjacent numbers in the same
direction (up, down, left, right or diagonally) in the 10 x 10 grid?
- What is the greatest product of three adjacent numbers in the same direction (up,
down, left, right or diagonally) in the 10 x 10 grid?
    
    Example: The product of these numbers is 4 x 60 x 11 = 2640.
    
**Note: Possible directions and their simplified direction (row, col) form to calculate the product:
- Up                    |   (up)             |   (row >= continous_integers - 1)                                                         | Direction: (0, -1)                        
- Down                  |   (down)           |   (row <= rows_count - continous_integers)                                                | Direction: (0, 1)
- Left                  |   (left)           |   (col >= continous_integers - 1)                                                         | Direction: (-1, 0)
- Right                 |   (right)          |   (col <= cols_count - continous_integers)                                                | Direction: (1, 0)
- Diagonal Right Down   |   (down_right)     |   (row <= rows_count - continous_integers and col <= cols_count - continous_integers)     | Direction: (1, 1)
- Diagonal Left Down    |   (down_left)      |   (row <= rows_count - continous_integers and col >= continous_integers - 1)              | Direction: (-1, 1)    
- Diagonal Right Up     |   (up_right)       |   (row >= continous_integers - 1 and col <= cols_count - continous_integers)              | Direction: (1, -1)        
- Diagonal Left Up      |   (up_left)        |   (row >= continous_integers - 1 and col >= continous_integers - 1)                       | Direction: (-1, -1)
"""
import argparse
import sys
from typing import List

NumberGrid = List[List[int]]

def main():
    parser = argparse.ArgumentParser(description="Find greatest product in a grid.")
    parser.add_argument("--path", type=str, required=True, help="Path to grid text file")
    parser.add_argument("--length", type=int, default=3, help="Number of contiguous integers (default: 3)")

    args = parser.parse_args()

    grid = []
    with open(args.path, "r") as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            grid.append(row)
    result = find_greatest_product_of_contiguous_integers(grid, args.length)
    print(f"Greatest product of {args.length} adjacent numbers is: {result}")

def find_greatest_product_of_contiguous_integers(grid: NumberGrid, continous_integers: int = 3) -> int:
    """
    Find the greatest product of three adjacent numbers in the same direction (up,
    down, left, right or diagonally) in the 10 x 10 grid.
        
    **Continous integers (the number of adjacent numbers) is 3 by default.
    
    return the product of the greatest product, and the number of combinations.
    """

    # To avoid duplicates, we only need to check one direction per position in the grid.
    directions = ["down", "right", "down_right", "up_right"]
    # number of rows in the grid
    rows_count = len(grid)
    
    # number of columns in the grid
    cols_count = len(grid[0])
    
    # max product and combination count
    max_product = 0
    combination_count = 0

       
    # Iterate over the grid 
    for row in range(rows_count):
        for col in range(cols_count):
            # print position and value
            for direction in directions:
                if is_direction_possible(row, col, rows_count, cols_count, direction, continous_integers):
                    combination_count += 1
                    product = calculate_product_of_continuous_integers(grid, row, col, direction, continous_integers)
                    if product > max_product:
                        max_product = product
        
    print(f"Combination count with duplicates: {combination_count}")
    return max_product


def is_direction_possible(row: int, col: int, rows_count: int, cols_count: int, direction: str, continous_integers: int) -> bool:
    """
    Check if a direction is possible for a given position in the grid.
    
    **Note: All Possible directions (however, to avoid duplicates, we only nee
    d to check one direction for each position):
    - Up                    |   (up)             |   (row >= continous_integers - 1)
    - Down                  |   (down)           |   (row <= rows_count - continous_integers)
    - Left                  |   (left)           |   (col >= continous_integers - 1)
    - Right                 |   (right)          |   (col <= cols_count - continous_integers)
    - Diagonal Right Down   |   (down_right)     |   (row <= rows_count - continous_integers and col <= cols_count - continous_integers)
    - Diagonal Left Down    |   (down_left)      |   (row <= rows_count - continous_integers and col >= continous_integers - 1)
    - Diagonal Right Up     |   (up_right)       |   (row >= continous_integers - 1 and col <= cols_count - continous_integers)
    - Diagonal Left Up      |   (up_left)        |   (row >= continous_integers - 1 and col >= continous_integers - 1)
    """

    match direction:
        case "up":
            return row >= continous_integers - 1
        case "down":
            return row <= rows_count - continous_integers
        case "left":
            return col >= continous_integers - 1
        case "right":
            return col <= cols_count - continous_integers
        case "down_right":
            return row <= rows_count - continous_integers and col <= cols_count - continous_integers
        case "down_left":
            return row <= rows_count - continous_integers and col >= continous_integers - 1
        case "up_right":
            return row >= continous_integers - 1 and col <= cols_count - continous_integers
        case "up_left":
            return row >= continous_integers - 1 and col >= continous_integers - 1
        case _:
            print(f"Invalid direction: {direction}")
            return False


def calculate_product_of_continuous_integers(grid: NumberGrid, row: int, col: int, direction: str, continous_integers: int) -> int:
    """
    Get the product of three adjacent numbers in the same direction.
        
    **Note: Possible directions and their simplified direction (row, col) form to calculate the product:
    **Consideration: To avoid duplicate combinations, you only need to check one direction per position in the grid.

    - Up                    |   (up)            | Direction: (-1, 0)  | Remove for duplicates combinations
    - Left                  |   (left)          | Direction: (0, -1)  | Remove for duplicates combinations
    - Diagonal Left Down    |   (down_left)     | Direction: (1, -1)  | Remove for duplicates combinations  
    - Diagonal Left Up      |   (up_left)       | Direction: (-1, -1)| Remove for duplicates combinations

    - Down                  |   (down)          | Direction: (1, 0)   
    - Right                 |   (right)         | Direction: (0, 1)   
    - Diagonal Right Down   |   (down_right)    | Direction: (1, 1)
    - Diagonal Right Up     |   (up_right)      | Direction: (-1, 1)        
    
    """
    DIRECTIONS = {   
    "down": (1, 0),                   
    "right": (0, 1),         
    "down_right": (1, 1),    
    "up_right": (-1, 1),      
    }
    
    row_direction, col_direction = DIRECTIONS[direction]

    product = 1
    for offset in range(continous_integers):
        r = row + offset * row_direction
        c = col + offset * col_direction
        product *= grid[r][c]
        
    return product


if __name__ == "__main__":
    main()


