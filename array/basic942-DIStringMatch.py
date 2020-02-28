class Solution:
    '''
    思路：IDID，res有5个数，生成第一个数时，看第一个符号若为I, append 0，保存下来MIN，以后最小的数得大于它;生成第二个数时，看第二个符号，若为D，则取最大数
    '''
    def diStringMatch(self, S: str) -> List[int]:
        if not S: return []
        res, N = [], len(S)
        pre_min, pre_max = -1, N+1
        for i in range(N):
            if S[i]=='I':
                res.append(pre_min+1)
                pre_min += 1
            else:
                res.append(pre_max-1)
                pre_max -= 1
        res.append(pre_min+1)
        return res
        
