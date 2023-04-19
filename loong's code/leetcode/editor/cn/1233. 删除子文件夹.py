from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for i in folder[1:]:
            m, n = len(ans[-1]), len(i)
            # 如果它的长度大于等于答案数组中最后一个文件夹的长度，并且它的前缀包含答案数组的最后一个文件夹再加上一个 /
            if m >= n or not (ans[-1] == i[:m]):
                ans.append(i)
        print(folder)
        return ans


class Trie:
    def __init__(self):
        self.children = {}
        self.fid = -1

    def insert(self, i, f):
        node = self
        ps = f.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.fid = 1

    def search(self):
        def dfs(root):
            if root.fid != -1:
                ans.append(root.fid)
                return
            for child in root.children.values():
                dfs(child)
        ans = []
        dfs(self)
        return ans



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for i, f in enumerate(folder):
            trie.insert(i, f)
        return [folder[i] for i in trie.search()]
print(Solution.removeSubfolders(Solution(), folder=["/a/b/c","/a/b/ca","/a/b/d"]))
