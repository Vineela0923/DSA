class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n
        arr = sum(grid, [])
        arr = arr[-k:] + arr[:-k] if k else arr        
        return [arr[i:i+n] for i in range(0, m*n, n)]