class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        top_num = []
        for num in nums:
            num_dict[num] += 1
        
        sorted_nums = sorted(num_dict, key=lambda x: num_dict[x], reverse=True)

        return sorted_nums[:k]
          
