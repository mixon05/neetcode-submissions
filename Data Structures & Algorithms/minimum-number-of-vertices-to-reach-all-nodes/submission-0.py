class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = [False] * n
        for _, end in edges:
            result[end] = True
        return [i for i, x in enumerate(result) if not x]