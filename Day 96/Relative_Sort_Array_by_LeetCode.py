# 1122. Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []
        for num in arr2:
            result.extend([num] * count[num]) # for example,. [2] * 3 = [2,2,2]
            del count[num]

        remaining_elements = []
        for num, freq in count.items():
            remaining_elements.extend([num] * freq)

        result.extend(sorted(remaining_elements))

        return result
