class Solution(object):
    '''
    思路1：中括号从内向外扩散，可以用3堆栈保存数字，中括号和字符，但维护起来需要同时注意好几个东西。
          也可以维护一个堆栈。
    '''
    # 来了每个字符无脑入堆栈，出的时候再控制流程。忽略了比如'100'这个数有3个字符组成，增加了出堆栈时的逻辑复杂度
    # 也可以入堆栈时就把'100'凑成一个单位入，还有类似'abc'也凑成一个单位入堆，而不是一个一个无脑入 
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res = [], ''
        for char in s:
            if char == ']':
                decoded_s, k = '', ''
                while stack[-1] is not '[': # decode one current k[encoded_s]
                    decoded_s = stack.pop() + decoded_s
                stack.pop()
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                decoded_s = k*decoded_s
                while stack and stack[-1] is not '[':#必须当下消掉前面的不带括号的字母，
                    stack[-1] += decoded_s  #否则留到后面搞不清楚这些字母的前后顺序
                    decoded_s = stack.pop()
                if not stack:
                    res += decoded_s
                else:
                    stack.append(decoded_s)
            else:
                stack.append(char)
        tmp = ''
        while stack:
            tmp = stack.pop() + tmp
        return res+tmp
