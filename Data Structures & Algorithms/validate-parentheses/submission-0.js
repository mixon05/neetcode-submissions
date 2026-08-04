class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = new Array()
        for (let i = 0; i < s.length; i++) {
            const popValue = stack[stack.length - 1]

            if (popValue === '{' && s[i] === '}') stack.pop()
            else if (popValue === '[' && s[i] === ']') stack.pop()
            else if (popValue === '(' && s[i] === ')') stack.pop()
            else stack.push(s[i])
        }

        return stack.length === 0
    }
}
