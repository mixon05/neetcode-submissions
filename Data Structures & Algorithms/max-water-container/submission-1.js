class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let i = 0
        let j = heights.length - 1
        let result = 0
        while (i < j) {
            const amount = Math.min(heights[i], heights[j]) * (j - i)
            result = Math.max(result, amount)
            if (heights[i] < heights[j]) {
                i++
            } else {
                j--
            }
        }
        return result
    }
}
