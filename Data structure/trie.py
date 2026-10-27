class TrieNode:
    __slots__ = ("children", "end_count", "prefix_count")

    def __init__(self):
        # 次の文字 -> TrieNode
        self.children = {}

        # このノードで終了する文字列の個数
        self.end_count = 0

        # このノードを通る文字列の個数
        self.prefix_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.distinct_count = 0

    def insert(self, word: str) -> None:
        """
        word を追加する。
        同じ文字列を複数回追加可能。

        Time: O(len(word))
        """
        node = self.root
        node.prefix_count += 1

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]
            node.prefix_count += 1

        # 初めて登録される文字列
        if node.end_count == 0:
            self.distinct_count += 1

        node.end_count += 1

    def erase(self, word: str) -> bool:
        """
        word を1つ削除する。

        word が存在する場合:
            1つ削除して True を返す。

        word が存在しない場合:
            何もせず False を返す。

        Time: O(len(word))
        """
        node = self.root
        path = []

        for c in word:
            if c not in node.children:
                return False

            parent = node
            node = node.children[c]

            # (親ノード, 文字, 子ノード)
            path.append((parent, c, node))

        if node.end_count == 0:
            return False

        node.end_count -= 1

        if node.end_count == 0:
            self.distinct_count -= 1

        self.root.prefix_count -= 1

        for _, _, child in path:
            child.prefix_count -= 1

        # 不要になったノードを削除
        for parent, c, child in reversed(path):
            if child.prefix_count == 0:
                del parent.children[c]
            else:
                break

        return True

    def count(self, word: str) -> int:
        """
        word が何個登録されているかを返す。

        Time: O(len(word))
        """
        node = self.root

        for c in word:
            if c not in node.children:
                return 0

            node = node.children[c]

        return node.end_count

    def search(self, word: str) -> bool:
        """
        word が存在するか。

        Time: O(len(word))
        """
        return self.count(word) > 0

    def count_prefix(self, prefix: str) -> int:
        """
        prefix から始まる文字列が何個存在するかを返す。
        重複も数える。

        Time: O(len(prefix))
        """
        node = self.root

        for c in prefix:
            if c not in node.children:
                return 0

            node = node.children[c]

        return node.prefix_count

    def starts_with(self, prefix: str) -> bool:
        """
        prefix から始まる文字列が存在するか。

        Time: O(len(prefix))
        """
        return self.count_prefix(prefix) > 0

    def count_distinct(self) -> int:
        """
        異なる文字列の種類数を返す。

        Time: O(1)
        """
        return self.distinct_count

    def __len__(self) -> int:
        """
        登録されている文字列の総数を返す。
        重複も数える。

        Time: O(1)
        """
        return self.root.prefix_count

    def __contains__(self, word: str) -> bool:
        """
        word in trie を使えるようにする。
        """
        return self.search(word)
