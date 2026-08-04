class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let left = 0
        let right = nums.length - 1
        while (left <= right) {
            const idx = Math.floor((left + right) / 2)
            if (nums[idx] < target) left = idx + 1
            else if (nums[idx] > target) right = idx - 1
            else return idx
        }
        return -1
    }
}
