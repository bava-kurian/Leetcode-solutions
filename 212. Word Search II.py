class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # store complete word at the end

        self.result = []
        rows, cols = len(board), len(board[0])

        # Step 2: DFS
        def dfs(r, c, node):
            letter = board[r][c]
            curr_node = node.children[letter]

            # Found a word
            if curr_node.word:
                self.result.append(curr_node.word)
                curr_node.word = None  # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in curr_node.children:
                        dfs(nr, nc, curr_node)

            # Restore letter
            board[r][c] = letter

            # Optional optimization: prune empty nodes
            if not curr_node.children:
                node.children.pop(letter)

        # Step 3: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return self.result
