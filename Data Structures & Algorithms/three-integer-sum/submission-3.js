class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b)

        const result = new Array()
        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue
            let j = i + 1
            let k = nums.length - 1
            while (j < k) {
                const value = nums[i] + nums[j] + nums[k]
                if (value < 0) j++
                else if (value > 0) k--
                else {
                    result.push([nums[i], nums[j], nums[k]])
                    j++
                    k--
                    while (j < k && nums[j] == nums[j - 1]) {
                        j++
                    }
                }
                
            }
        }
        return result
    }
}
