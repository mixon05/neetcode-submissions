class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false
        const arr1 = s.split('')
        const map = new Map()
        for (let c of arr1) {
            if (map.has(c)) {
                map.set(c, map.get(c) + 1) 
            } else {
                map.set(c, 1)
            }
        }
        const arr2 = t.split('')
        for (let d of arr2) {
            if (!map.has(d) || map.get(d) === 0) {
                return false
            } else {
                map.set(d, map.get(d) - 1)
            }
        }
        return true
    }
}
