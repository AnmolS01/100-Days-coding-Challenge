# Problem Statement: 752. Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
    
        visited = set(["0000"])
        queue = deque([("0000", 0)])
    
        while queue:
            current, steps = queue.popleft()
            for i in range(4):
                for j in [-1, 1]:
                    new_digit = (int(current[i]) + j) % 10
                    new_lock = current[:i] + str(new_digit) + current[i+1:]
                    if new_lock == target:
                        return steps + 1
                    if new_lock not in visited and new_lock not in deadends:
                        visited.add(new_lock)
                        queue.append((new_lock, steps + 1))
    
        return -1
