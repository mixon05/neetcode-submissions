class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        res = []

        def dfs(i):
            res.append(i)

            for j, parent in enumerate(ppid):
                if parent == i:
                    dfs(pid[j])

        dfs(kill)
        return res