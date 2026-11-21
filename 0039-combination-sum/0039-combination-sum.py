from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack(index: int, total: int) -> None:
            if total == target:
                result.append(current.copy())
                return

            if total > target or index >= len(candidates):
                return

            current.append(candidates[index])
            backtrack(index, total + candidates[index])
            current.pop()

            backtrack(index + 1, total)

        backtrack(0, 0)
        return result