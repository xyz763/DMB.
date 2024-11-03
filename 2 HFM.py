class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

def printNodes(node, val=''):
    if not node.left and not node.right:
        print(f"{node.symbol} -> {val}")
    else:
        printNodes(node.left, val + '0')
        printNodes(node.right, val + '1')

chars, freq = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], [4, 7, 12, 14, 17, 43, 54]
nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    nodes.append(Node(nodes[0].freq + nodes[1].freq, '', nodes.pop(0), nodes.pop(0)))

printNodes(nodes[0])