# Grid Combination Parser

This script analyzes a grid of integers to: 1. How many different combinations are there of three adjacent numbers in the same
direction (up, down, left, right or diagonally) in the 10 x 10 grid? 2. What is the greatest product of three adjacent numbers in the same direction (up,
down, left, right or diagonally) in the 10 x 10 grid?

## Requirements

Submit your answers to each of the above questions along with a link to your source code. The
solution should be submitted in Python.
Your source code will be held in GitHub and should contain a function which accepts a grid of
size n x m and finds the greatest product of x adjacent numbers in the same direction. We will
be running a large grid (much larger than the above example) through your method. In Python,
the function signature could look like the following:
def find_greatest_product_of_contiguous_integers(grid: NumberGrid,
contiguous_integers: int) -> int:
Please also attach any relevant notes/comments along with your submission. Clean, readable,
testable code is preferred.

## Clarifications

- Supports 4 directions to avoid duplicate combinations:
  - Right
  - Down
  - Diagonal down-right
  - Diagonal up-right
- Fully tested with `pytest`
- CLI support to run against any grid file

### Usage

```bash
python src/main.py --path grid.txt --length 3
```
