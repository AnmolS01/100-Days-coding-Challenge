# Problem Statement: 79. Word Search

class Solution:
    # Check if the word exists on the board
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        # Loop through each cell of the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]: # Check if the first character of the word matches the current cell
                   
                    if self.findWord(board, word, i, j, 0): # If the first character matches, attempt to find the word starting from this cell
                        return True
                      
        # If the word is not found starting from any cell, return False
        return False

    # Recursive function to find the word on the board starting from a given cell
    def findWord(self, board, word, row, column, wordIndex):
        # if all characters of the word have been matched, return True
        if wordIndex == len(word):
            return True
          
        # Check if the current cell is out of bounds
        if (row < 0 or column < 0 or row >= len(board) or column >= len(board[0])):
            return False
          
        # Check if the current cell does not match the current character of the word
        if (board[row][column] == ' ' or board[row][column] != word[wordIndex]):
            return False
          
        # Temporarily mark the current cell as visited
        char = board[row][column]
        board[row][column] = ' '
      
        # Recursively check neighboring cells for the next character of the word
        if ((self.findWord(board, word, row-1, column, wordIndex+1) or
             self.findWord(board, word, row, column+1, wordIndex+1) or
             self.findWord(board, word, row+1, column, wordIndex+1) or
             self.findWord(board, word, row, column-1, wordIndex+1))):
            return True
        # Backtrack: restore the original character of the current cell
        board[row][column] = char
      
        # If the word cannot be found starting from the current cell, return False
        return False
