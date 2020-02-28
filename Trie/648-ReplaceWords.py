class Solution:
    '''
    思路1：为每个词搜索，Time O(KN), Space O(1)
    思路2：字典树
    '''
    def replaceWords(self, dict, sentence):
        root, end_of_word = {}, '#'
        for word in dict:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[end_of_word] = end_of_word
            
        words = sentence.split()
        node = root
        for i in range(len(words)):
            tmp, node = '', root
            for letter in words[i]:
                if letter not in node or end_of_word in node:
                    break
                else:
                    tmp += letter
                    node = node[letter]
            if end_of_word in node:
                words[i] = tmp
        return ' '.join(words)
                 
    def replaceWords1(self, dict: List[str], sentence: str) -> str:
        words = sentence.split()
        for i in range(len(words)):
            min_len = float('inf')
            for root in dict:
                if root == words[i][:len(root)] and len(root)<min_len:
                    words[i] = root
                    min_len = len(root)
        return ' '.join(words)
