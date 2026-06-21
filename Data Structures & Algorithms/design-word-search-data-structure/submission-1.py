class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for x in node.children.values():
                        if dfs(i + 1, x):
                            return True
                    return False
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.endOfWord
        return dfs(0, self.root)