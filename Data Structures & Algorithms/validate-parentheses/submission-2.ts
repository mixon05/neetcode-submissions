class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(str: string): boolean {
        const arr: string[] = [];
        for (let s of str) {
            if (s === '(' || s === '[' || s === '{') arr.push(s)
            else if (s === ')' && arr.at(-1) === '(') arr.pop()
            else if (s === ']' && arr.at(-1) === '[') arr.pop()
            else if (s === '}' && arr.at(-1) === '{') arr.pop()
            else return false
        }
        return arr.length <= 0
    }
}
