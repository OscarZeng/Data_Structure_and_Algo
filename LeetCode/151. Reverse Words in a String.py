class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        print(s)
        while s.find('  ') != -1:
            s = s.replace('  ',' ')
        print(s)
        sList = s.split(' ')
        print(sList)
        return ' '.join(sList[::-1])