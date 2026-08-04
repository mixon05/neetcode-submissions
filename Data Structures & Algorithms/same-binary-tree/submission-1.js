class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        if (!p && !q) {
            return true
        } else if (!p || !q) {
            return false
        } else if (p.val !== q.val) {
            return false
        }

        const isLeft = this.isSameTree(p.left, q.left)
        const isRight = this.isSameTree(p.right, q.right)

        return isLeft && isRight
    }
}