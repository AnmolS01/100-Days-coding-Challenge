# Problem Statement: 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        n = max(len(ver1), len(ver2))

        for i in range(n):
            if i < len(ver1):
                revision1 = int(ver1[i])
            else:
                revision1 = 0

            if i < len(ver2):
                revision2 = int(ver2[i])
            else:
                revision2 = 0

            if revision1 > revision2:
                return 1
            elif revision1 < revision2:
                return -1
        return 0
