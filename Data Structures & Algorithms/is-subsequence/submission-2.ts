class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isSubsequence(s: string, t: string): boolean {
        let i = 0
        let j = 0
        while (i < s.length) {
            if (j === t.length) { return false }
            else if (s[i] === t[j]) {
                i++
                j++
            } else {
                j++
            }
        }
        return true
    }
}
