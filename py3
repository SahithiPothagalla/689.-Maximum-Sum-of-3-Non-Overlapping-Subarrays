class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        acc = [0] + list(accumulate(nums))
        @cache
        def dp(i, rem):
            if rem == 0: return 0, []
            if len(nums) - i < k: return -math.inf, []
            choose_i, indices_1 = dp(i + k, rem - 1)
            choose_i += acc[i + k] - acc[i]
            not_choose_i, indices_2 = dp(i + 1, rem)
            return (choose_i, [i] + indices_1) if choose_i >= not_choose_i else (not_choose_i, indices_2)
        return dp(0, 3)[1]
