class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = int(board[r][c]) - 1
                    mask = 1 << num
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + c // 3] |= mask
        def backtrack(idx):
            if idx == len(empty):
                return True
            r, c = empty[idx]
            box = (r // 3) * 3 + c // 3
            available = ~(rows[r] | cols[c] | boxes[box]) & 0x1FF
            while available:
                bit = available & -available
                digit = bit.bit_length()
                board[r][c] = str(digit)
                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit
                if backtrack(idx + 1):
                    return True
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box] ^= bit
                available &= available - 1
            board[r][c] = "."
            return False
        backtrack(0)  