class Solution:
    '''
    思路：stack保存前面的坐括号，后面右括号匹配的话出栈。Time O(n) Space O(n)
    '''
    def isValid(self, s: str) -> bool:
        stack = []
        paired = dict(zip([')',']', '}'], ['(','[','{']))
        for char in s:
            if stack and (char in paired) and stack[-1]==paired[char]:
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False
