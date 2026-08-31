class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# submission 1902430140 - 2026-01-30T21:58:57+00:00
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# submission 1902430491 - 2026-01-30T21:59:56+00:00
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node = node.children[char]
                node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# submission 1902430550 - 2026-01-30T22:00:06+00:00
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node = node.children[char]
            
            node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# submission 1902431706 - 2026-01-30T22:03:26+00:00
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# submission 1902431795 - 2026-01-30T22:03:43+00:00
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endword = True

        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endword

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True 
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        
        return dfs(self.root, 0)


            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)