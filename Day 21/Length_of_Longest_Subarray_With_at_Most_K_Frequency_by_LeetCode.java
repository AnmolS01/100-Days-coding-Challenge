// Problem Statement2958. Length of Longest Subarray With at Most K Frequency

class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        int n = nums.length;
        int maxLength = 0;
        int start = 0;
        int end = 0;
        HashMap<Integer, Integer> frequency = new HashMap<>();

        while (end < n) {
            frequency.put(nums[end], frequency.getOrDefault(nums[end], 0) + 1);

            while (frequency.get(nums[end]) > k) {
                frequency.put(nums[start], frequency.get(nums[start]) - 1);
                start++;
            }

            maxLength = Math.max(maxLength, end - start + 1);
            end++;
        }
        return maxLength;
    }
}
