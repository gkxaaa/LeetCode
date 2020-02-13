# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    '''
    思路1：遍历整个列表把所有数字按顺序入栈，最后按顺序出栈,需要额外内存和时间不符
           合迭代器特性。Time O(2*n), Space O(2*n)
    思路2: 队列。hasNext方法每次检查第一个元素是否为列表，若是去掉括号重新入队列，
           直到是整数返回True。next方法每次出队列首元素。核心思想就在于出队列首元
           素若为列表时，剥掉列表括号重新将元素入队列。Time O(n) Space O(n)
    '''
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = nestedList
        
    def next(self) -> int:
        return self.queue.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        while self.queue:
            top = self.queue[0]
            if top.isInteger():
                return True
            self.queue = top.getList() + self.queue[1:]
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
