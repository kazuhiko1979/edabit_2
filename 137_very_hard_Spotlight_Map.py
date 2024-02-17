"""
Spotlight Map
Given a grid of numbers, return a grid of the Spotlight Sum of each number. The spotlight sum can be defined as the total of all numbers immediately surrounding the number on the grid, including the number in the total.

Examples
spotlight_map([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [12, 21, 16],
  [27, 45, 33],
  [24, 39, 28]
]


spotlight_map([
  [2, 6, 1, 3, 7],
  [8, 5, 9, 4, 0]
]) ➞ [
  [21, 31, 28, 24, 14],
  [21, 31, 28, 24, 14]
]


spotlightMap([[3]]) ➞ [[3]]
Notes
Note that all numbers have a spotlight sum, including numbers on the edges.
All inputs will be valid grid (all rows will have the same length).
"""


def spotlight_map(grid):
  # Get the dimensions of the grid
  rows = len(grid)
  cols = len(grid[0])

  # Initialize the result grid with zeros
  result = [[0] * cols for _ in range(rows)]

  # Iterate through each cell in the grid
  for i in range(rows):
    for j in range(cols):
      # Calculate the spotlight sum for the current cell
      spotlight_sum = 0
      for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
          # Check boundary conditions
          if 0 <= x < rows and 0 <= y < cols:
            spotlight_sum += grid[x][y]

      # Update the result grid with the spotlight sum
      result[i][j] = spotlight_sum

  return result

# import numpy as np
#
# def spotlight_map(grid):
#   if not grid: return grid
#   g = np.array(grid)
#   h, w = g.shape
#   return [[np.sum(g[max((i-1, 0)):min((i+2, h)), max((j-1, 0)):min((j+2, w))]) for j in range(w)] for i in range(h)]


print(spotlight_map([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(spotlight_map([
  [2, 6, 1, 3, 7],
  [8, 5, 9, 4, 0]
]))
