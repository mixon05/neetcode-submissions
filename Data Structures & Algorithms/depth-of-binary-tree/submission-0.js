/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {

        function maxD(root, val) {
            if (!root) return val

            const left = maxD(root.left, val+1)
            const right = maxD(root.right, val+1)

            return Math.max(left, right)
        }

        return maxD(root, 0)
    }
}
