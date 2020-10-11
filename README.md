# How to play Sudoku
Sudoku is played on a grid of 9 x 9 spaces. Within the rows and columns are 9 “squares” (made up of 3 x 3 spaces). Each row, column and square (9 spaces each) needs to be filled out with the numbers 1-9, without repeating any numbers within the row, column or square.



# <h1>Apply Backtracking Algorithm
We want to avoid using the Naive Approach (try out every possible value to acquire a solution) due to having to possibly run 9<sup>81</sup> possibilities due to having a 9x9 grid with 9 possible values within in cell.

We want to use a backtracking approach to help solve this problem. The approach is as such:
1. Pick an empty cell
2. Try all numbers
3. Find one that works
4. If <b>3</b> worked, then repeat process for rest of board
5. Backtrack as soon as a solution cannot be completed

The goal is to complete one cell at a time and recursively checking that the solutions work until you get to one that does work. This approach is a lot faster than the Naive Approach due to not having to compute 9<sup>81</sup> calculations.

# Programmatic Approch
For each of the steps listed, we should be able to create an function/file dedicated for each.
1. Create a function to find the empty cells
2. Function to try/iterate through all numbers
3. Check current solution/Check if the number we put in is valid
4. Reset the value when a solution is not correct

