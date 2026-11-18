class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        res = [kill]
        children = defaultdict(list)
        for i, parent in enumerate(ppid):
            children[parent].append(pid[i])

        queue = children[kill]
        while queue:
            child = queue.pop()
            res.append(child)
            for ch in children[child]:
                queue.append(ch)

        return res