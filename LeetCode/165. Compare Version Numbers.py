class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1 == version2:
            return 0
        version1IntList = version1.split('.')
        version2IntList = version2.split('.')
        print(version1IntList, version2IntList)
        
        while len(version1IntList) != 0 or len(version2IntList) != 0:
            if len(version1IntList) == 0:
                v1First = 0
            else:
                v1First = int(version1IntList.pop(0))
            if len(version2IntList) == 0:
                v2First = 0
            else:
                v2First =int(version2IntList.pop(0))
            print(v1First, v2First)
            if v1First == v2First:
                continue
            elif v1First > v2First:
                return 1
            else:
                return -1
        return 0

            