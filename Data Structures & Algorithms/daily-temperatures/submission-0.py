class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append((t, i))
        
        return result
            