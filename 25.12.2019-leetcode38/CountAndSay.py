class Solution(object):
    '''
    这是一道for遍历并考虑corner case的题，关键在于对程序步骤有清晰的把控。
    思路1: 从n=1开始递增到目标值，迭代。每次迭代可以用space O(1), 
           构建一个字典记录当前key的重复次数，一旦出现没见过的key，
           结束本次迭代，写下答案。
    思路2：也可不用字典，用一个while循环记录当前数字重复的次数
    '''   
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for _ in range(1,n):
            count, tmp = 1, ''
            for i in range(1,len(seq)+1):
                if i<len(seq) and seq[i]==seq[i-1]:
                    count += 1
                else:
                    tmp += str(count)+seq[i-1]
                    count = 1
            seq = tmp
        return seq
                
