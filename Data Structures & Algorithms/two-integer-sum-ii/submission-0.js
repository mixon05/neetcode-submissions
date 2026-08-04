class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i = 0
        let j = numbers.length - 1
        while (true) {
            const sum = numbers[i] + numbers[j]
            if (sum < target) {
                i++
            } else if (sum > target) {
                j--
            } else {
                return [i + 1, j + 1]
            }
        }
    }
}
