class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = set(nums)
        pairs = {a ^ b for a in vals for b in vals}
        return len({p ^ x for p in pairs for x in vals})