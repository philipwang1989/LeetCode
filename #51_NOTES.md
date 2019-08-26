# Leetcode 51

Problem statement: 
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

This is a classic search/recursion problem.

Idea is as follows:

![explanation](image_51_1.png)

## Before we start

One keep aspect of Python (given `a` and `b`, each is a python object of type `int`) coding one needs to understand is the difference between when parse it directly into a function without assigning these to a new object:

1. `a.append(b)`
2. `a + [b]`

Here we use `print()` as the example:

```python
a = []
b = 5
print(a + [b])
# return [5]
print(a.append(b))
# return None
```

First operation (`+`) create a new item without modifying the original items whereas the second operation modifies the original item.

## Backtracking

Ovearll, backtracking runs like the following:

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

From Leetcode hint for # 52, backtracking in this problem can be best understood as such:

```python
def backtrack_nqueen(row = 0, count = 0):
    for col in range(n):
        # iterate through columns at the curent row.
        if is_not_under_attack(row, col):
            # explore this partial candidate solution, and mark the attacking zone
            place_queen(row, col)
            if row + 1 == n:
                # we reach the bottom, i.e. we find a solution!
                count += 1
            else:
                # we move on to the next row
                count = backtrack(row + 1, count)
            # backtrack, i.e. remove the queen and remove the attacking zone.
            remove_queen(row, col)
    return count
```

The fact that the algorithm moves to next row BEFORE removing the queen, it is equivalent to running a DFS.

To solve the problem we need first a search function:

```python
    def search(self, n, cols, result):
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return

        for col in range(n):
            if not self.isValid(cols, col):
                continue
            self.search(n, cols + [col], result)
```

**result** is a global variable that stores the solutions generated from each of the DFS searchs.
**Cols** stores the position of QUEEN in each row.

If the total number of QUEENS placed in cols equals to n, we have a solution and therefore append the cols. Otherwise the loop continues to check if current (row, col) combination is a valid position to place a QUEEN.

Next we need the most important function - isValid:

```python
def isValid(self, cols, col):
    currentRowNumber = len(cols)
    for i in range(currentRowNumber):
        # same column
        if cols[i] == col:
            return False
        # left-top to right-bottom
        if col - cols[i] == currentRowNumber - i:
            return False
        # right-top to left-bottom
        if col - cols[i] == -(currentRowNumber - i):
            return False
    return True
```

For each given (cols-which is the row, col), we look for any encounter of attacks from previously placed QUEENS.
Again, **cols** keep track of the position of the QUEEN.

## Solution

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n <= 0:
            return result

        cols = []
        self.search(n, cols, result)
        return result

    def search(self, n, cols, result):
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return

        for col in range(n):
            if not self.isValid(cols, col):
                continue
            self.search(n, cols + [col], result)

    def isValid(self, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # same column
            if cols[i] == col:
                return False
            # left-top to right-bottom
            if col - cols[i] == currentRowNumber - i:
                return False
            # right-top to left-bottom
            if col - cols[i] == -(currentRowNumber - i):
                return False
        return True
    def drawBoard(self, cols):
        board = []
        for i in range(len(cols)):
            line = ""
            for j in range(len(cols)):
                if j == cols[i]:
                    line += "Q"
                else:
                    line += "."
            board.append(line)
        return board
```

