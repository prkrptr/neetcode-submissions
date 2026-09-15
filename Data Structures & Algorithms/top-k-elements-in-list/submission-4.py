class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        k_dict = defaultdict(int)

        for i, num in enumerate(nums):
            k_dict[num] += 1

        return sorted(k_dict, key=k_dict.get, reverse=True)[:k]
        