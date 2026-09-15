class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        LENGTH = 9
        # remove periods
        board_copy = [[x for x in row if x != "."] for row in board ]


        for row in board_copy: # check duplicates in row
            if len(row) != len(set(row)):
                return False # found duplicates

        board_copy_t = zip(*board)
        for col in board_copy_t: # check duplicates in column
            nums = [x for x in col if x != "."]
            if len(nums) != len(set(nums)):
                return False
        
        # check 3x3
        for i in range (0, 9, 3):
            for j in range(0,9,3):
                block = []
                for k in range(i, i+3):
                    for y in range(j, j+3):
                        if board[k][y] != ".":
                            block.append(board[k][y])
                if len(block) != len(set(block)):
                    return False    
        
        return True
