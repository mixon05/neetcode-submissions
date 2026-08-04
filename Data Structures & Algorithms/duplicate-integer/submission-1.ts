class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const map = new Map()
        for (let n of nums) {
            if (!map.has(n)) {
                map.set(n, false)
            } else {
                return true
            }
        }
        return false
    }
}
