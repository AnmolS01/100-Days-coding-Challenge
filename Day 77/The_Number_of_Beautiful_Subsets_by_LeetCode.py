2597. The Number of Beautiful Subsets

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = []
        
        def generate_subsets(start, current_list):
            if start >= len(nums):
                if current_list:
                    result.append(current_list[:])
                return

            current_list.append(nums[start])
            generate_subsets(start + 1, current_list)
            current_list.pop()
            generate_subsets(start + 1, current_list)
        
        generate_subsets(0, [])
        
        def is_beautiful(subset):
            subset_set = set(subset)
            for num in subset:
                if (num + k) in subset_set or (num - k) in subset_set:
                    return False
            return True
        
        count = 0
        for subset in result:
            if is_beautiful(subset):
                count += 1
        
        return count
