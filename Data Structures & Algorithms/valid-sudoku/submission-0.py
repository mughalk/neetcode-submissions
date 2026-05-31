class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use python .isdigit
        # distinguish between column and row
        # a row is probably across the entire 9x9 board
        # a column is also across the entire 9x9 board
        # a sub-box is the list at board[i]
        # a digit or "." should be at board[i][j]
        # NO duplicates -> dictionary or set or hashmap, all the same
        # strat: create separate hashmap for rows, separate map for cols as you iterate through
        # optimize later
        row_map={}
        col_map={}
        square_map={}
        for row in range(0, len(board)):
            if row not in row_map:
                row_map[row]=[]
            for col in range(0, len(board[row])):
                if board[row][col]==".":
                    continue
                    # skip this loop iteration
                if col not in col_map:
                    col_map[col]=[]
                if (row//3,col//3) not in square_map:
                    square_map[row//3,col//3]=[]
                # kinda unsure abt the iterations here but wtv
                if board[row][col] in row_map[row] or board[row][col] in col_map[col] or board[row][col] in square_map[row//3,col//3]:
                    return False
                    #immediate exit
                row_map[row].append(board[row][col])
                col_map[col].append(board[row][col])
                # this will give smthng like 0,0 or 0,1, which acc yeah those will work
                # bc theyre coordinates
                square_map[row//3,col//3].append(board[row][col])
        # for x in range(0, len(board)):
        #     # no row has dupes
        #     if len(row_map[x])!=len(set(row_map[x])):
        #         return False
        #     # no col has dupes
        #     if len(col_map[x])!=len(set(col_map[x])):
        #         return False
        # SUB-BOX HAS NO DUPES
        return True
