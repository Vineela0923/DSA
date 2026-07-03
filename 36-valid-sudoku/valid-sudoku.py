class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    if ((r, num) in seen or
                        (num, c) in seen or
                        (r // 3, c // 3, num) in seen):
                        return False
                    seen.add((r, num))
                    seen.add((num, c))
                    seen.add((r // 3, c // 3, num))
        return True
        