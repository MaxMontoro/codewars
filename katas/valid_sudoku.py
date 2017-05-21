def validSolution(board):

    def contains_all_digits(array):
        return all(num in array for num in range(1,10))

    def flatten(square):
        return [item for sublist in square for item in sublist]

    for row in board:
        if not contains_all_digits(row):
            return False

    for column in range(len(board[0])):
        nums = [row[column] for row in board]

        if not contains_all_digits(nums):
            return False


    for num in range(3):
        nth = num*3
        square = [board[row][num*3: num*3+3] for row in range(3)]
        flattened = [item for sublist in square for item in sublist]
        if not contains_all_digits(flatten(square)):
            return False

    return True
