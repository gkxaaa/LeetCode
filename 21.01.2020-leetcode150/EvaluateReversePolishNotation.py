import operator
class Solution:
    '''
    思路：顺序遍历，遇到数字入栈，遇到符号，出栈两次计算结果并入栈。
          继续遍历直到遍历结束，栈内只剩一个数即为结果
          Time O(n) Space O(n)
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+' : operator.add,'-' : operator.sub, \
                 '*' : operator.mul,'/' : operator.truediv}
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()
                res = int(ops[token](b,a))
                stack.append(res)
        return stack.pop()
                
