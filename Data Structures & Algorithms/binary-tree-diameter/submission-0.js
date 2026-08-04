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
diameterOfBinaryTree(root) {
        let maxDiameter = 0;

        function calculateHeight(node) {
            if (!node) return 0;

            const leftH = calculateHeight(node.left);
            const rightH = calculateHeight(node.right);

            maxDiameter = Math.max(maxDiameter, leftH + rightH);

            return 1 + Math.max(leftH, rightH);
        }

        calculateHeight(root);
        return maxDiameter;
    }
}
