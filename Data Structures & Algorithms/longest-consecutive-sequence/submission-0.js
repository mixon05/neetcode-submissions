class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const s = new Set(nums)
        let res = 0
        for (let num of nums) {
            if (!s.has(num - 1)) {
                let i = num
                while (s.has(i)) {
                    res = Math.max(res, i - num + 1)
                    i++
                }
            }
        }
        return res
    }
}
