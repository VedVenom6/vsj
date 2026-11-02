# Unit V case study: ZIP/GZIP-style compression with a Huffman tree
# Repeatedly join the two LEAST frequent nodes (greedy). Frequent characters get shorter codes.

class Node:
    def __init__(self, freq, ch=None, left=None, right=None):
        self.freq = freq
        self.ch = ch
        self.left = left
        self.right = right


def build_huffman(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    nodes = [Node(f, c) for c, f in freq.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda n: n.freq)         # a priority queue would be O(log n) per step
        a = nodes.pop(0)
        b = nodes.pop(0)
        nodes.append(Node(a.freq + b.freq, None, a, b))
    return nodes[0], freq


def make_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node.ch is not None:                     # leaf
        codes[node.ch] = code or "0"
    else:
        make_codes(node.left, code + "0", codes)
        make_codes(node.right, code + "1", codes)
    return codes


def decode(root, bits):
    out, cur = "", root
    for b in bits:
        cur = cur.left if b == "0" else cur.right
        if cur.ch is not None:
            out += cur.ch
            cur = root
    return out


text = "abracadabra"
root, freq = build_huffman(text)
codes = make_codes(root)
for c in sorted(codes, key=lambda c: -freq[c]):
    print(f"  '{c}' freq {freq[c]}  code {codes[c]}")
encoded = "".join(codes[c] for c in text)
print("Encoded:", encoded)
print(f"Bits: {len(encoded)} vs {len(text) * 8} uncompressed")
print("Decoded:", decode(root, encoded))
