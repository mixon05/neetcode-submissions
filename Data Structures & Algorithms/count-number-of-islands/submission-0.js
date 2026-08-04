class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        if (!grid || grid.length === 0) return 0;

        const rows = grid.length
        const cols = grid[0].length

        const visited = new Set()
        let islands = 0

        const bfs = (startR, startC) => {
            const queue = [[startR, startC]]
            visited.add([startR, startC].join(','))

            while (queue.length !== 0) {
                const [row, col] = queue.shift() 
                
                const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for (const [dr, dc] of directions) {
                    const r = row + dr
                    const c = col + dc

                    if (r >= 0 && r < rows 
                    && c >= 0 && c < cols
                    && grid[r][c] === "1"
                    && !visited.has([r, c].join(','))) {
                        queue.push([r, c])
                        visited.add([r, c].join(','))
                    }
                }
            }
        }

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (grid[r][c] === "1" && !visited.has([r, c].join(','))) {
                    bfs(r, c)
                    islands++
                }
            }
        }
        return islands
    }
}