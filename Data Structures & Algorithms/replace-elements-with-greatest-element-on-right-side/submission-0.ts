class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr: number[]): number[] {
        const out = [...arr]
        for (let i = 0; i < out.length - 1; ++i) {
            let max = -1
            for (let j = i + 1; j < out.length; ++j) {
                max = Math.max(max, arr[j])
            }
            out[i] = max
        }
        out[out.length - 1] = -1
        return out
    }
}
