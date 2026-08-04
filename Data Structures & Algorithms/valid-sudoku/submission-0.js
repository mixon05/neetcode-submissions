class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const cols = Array.from({ length: 9 }, () => new Set())
        const rows = Array.from({ length: 9 }, () => new Set())
        const squares = Array.from({ length: 9 }, () => new Set())

        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                const val = board[r][c]
                if (val == ".") continue

                const squareIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3)

                if (rows[r].has(val) || 
                    cols[c].has(val) || 
                    squares[squareIndex].has(val)) {
                    return false
                }

                rows[r].add(val)
                cols[c].add(val)
                squares[squareIndex].add(val)
            }
        }
        return true
    }
}