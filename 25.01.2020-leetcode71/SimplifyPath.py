class Solution:
    '''
    已知： 1. /// --> /
           2. end position not /       
           3. only ../ and ./ or .. at the end needs to operate
    思路：问题关键在于只有出现../或./时需要改变临时结果。有以下情况
          1. 若当前字符为非斜杠直接入栈，若为斜杠，若栈末尾为斜杠continue，若栈末 
             尾字符不为点也入栈
          2. 若为斜杠
             2.1 若栈末尾为斜杠，continue
             2.2 若栈倒数第二个为斜杠，stack出栈
             2.3 若栈倒数第二个为点且倒数第三个为斜杠，出栈直到栈的上一个斜杠处
          最后去除末尾的斜杠，连接返回结果. Time O(n) Space O(n)
    '''
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path+'/': #help to process .. or . at the end position
            if s != '/' or not stack or (stack[-1]!='.' and stack[-1]!='/'):
                stack.append(s)
            else:
                if stack[-1]=='/': #process //
                    continue
                elif stack[-2]=='/': #process ./
                    stack.pop() 
                elif stack[-2]=='.' and stack[-3]=='/': #process ../
                    stack = stack[:-3]
                    while len(stack)>1 and stack[-1]!='/':
                        stack.pop()
                    if not stack: stack.append('/')
                else: # process /a.../ or /a..f..v/c
                    stack.append(s)
        res = ''.join(stack)
        return res if len(res)==1 or res[-1]!='/' else res[:-1]
                
                
    def simplifyPath2(self, path: str) -> str:
        stack1, stack2 = [], []
        for s in path:
            if s.isalpha():
                stack1.append(s)
            elif s=='.':
                stack2.append(s)
            else:
                if not stack1 or stack1[-1]!='/':
                    stack1.append(s)
                elif len(stack2)==2: # it means containing ".."
                    if len(stack1)>1: # keep the first "/"
                        stack1.pop()
                        stack1.pop()    
                elif len(stack2)>2:
                    continue
                stack2 = [] # if contains "." or nothing, pass
        if len(stack2)==2 and len(stack1)>1:
            stack1.pop()
            stack1.pop()
            stack2 = []
        if len(stack2)>2:
            res = ''.join(stack1+stack2)
        else:
            res = ''.join(stack1)
        return res if len(res)==1 or res[-1]!='/' else res[:-1]
            
                    
