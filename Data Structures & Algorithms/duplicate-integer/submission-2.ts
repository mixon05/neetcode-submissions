class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const set = new Set()
        for (let n of nums) {
            if (!set.has(n)) {
                set.add(n)
            } else return true
        }
        return false
    }
}
