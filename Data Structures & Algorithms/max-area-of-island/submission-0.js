class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const rows = grid.length
        const cols = grid[0].length

        const visited = new Set()
        let maxArea = 0

        const bfs = (startR, startC) => {
            const queue = [[startR, startC]]
            visited.add([startR, startC].join(","))

            let area = 1

            while (queue.length !== 0) {
                const [row, col] = queue.shift()

                const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for (const [dr, dc] of directions) {
                    const r = row + dr
                    const c = col + dc

                    if (r >= 0 && r < rows
                    && c >= 0 && c < cols
                    && grid[r][c] === 1
                    && !visited.has([r, c].join(","))) {
                        area++
                        queue.push([r, c])
                        visited.add([r, c].join(","))
                    }
                }
            }
            return area
        }

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (grid[r][c] === 1 && !visited.has([r, c].join(","))) {
                    const area = bfs(r, c)
                    maxArea = Math.max(maxArea, area)
                }
            }
        }
        return maxArea
    }
}
