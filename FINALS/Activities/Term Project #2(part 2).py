from LinkedBinaryTree import LinkedBinaryTree
def build_matrix(vertices, left_children, right_children):
    """Builds a binary tree from matrix representations."""
    tree = LinkedBinaryTree()
    nodes = {}

    root = tree._add_root(vertices[0])
    nodes[vertices[0]] = root

    for vertex, left, right in zip(vertices, left_children, right_children):
        current = nodes[vertex]

        if left != "-":
            left_node = tree._add_left(current, left)
            nodes[left] = left_node

        if right != "-":
            right_node = tree._add_right(current, right)
            nodes[right] = right_node

    return tree
def get_traversals(tree):
    """Returns the traversals of the binary tree."""
    root = tree.root()
    preorder = [p.element() for p in tree.preorder()]
    inorder = [p.element() for p in tree.inorder()]
    postorder = [p.element() for p in tree.postorder()]

    return {"Preorder": preorder, "Inorder": inorder, "Postorder": postorder}

trees_data = [
    {
        "vertices": ["r", "a", "b", "c", "d", "e", "f", "g", "h"],
        "left_children": ["a", "b", "-", "e", "-", "-", "-", "-", "-"],
        "right_children": ["-", "c", "d", "f", "-", "g", "-", "h", "-"],
    },
    {
        "vertices": ["r", "a", "b", "c", "d", "e", "f", "g"],
        "left_children": ["a", "c", "-", "-", "-", "-", "-", "-"],
        "right_children": ["b", "d", "e", "-", "-", "f", "g", "-"],
    },
    {
        "vertices": ["r", "a", "b", "c", "d", "e", "f"],
        "left_children": ["a", "-", "d", "f", "-", "-", "-"],
        "right_children": ["b", "c", "e", "-", "-", "-", "-"],
    },
    {
        "vertices": ["r", "a", "b", "c", "d", "e", "f", "g", "h", "i"],
        "left_children": ["a", "c", "e", "g", "-", "i", "-", "-", "-", "-"],
        "right_children": ["b", "d", "f", "h", "-", "-", "-", "-", "-", "-"],
    },
]

for i, data in enumerate(trees_data, start=1):
    tree = build_matrix(data["vertices"], data["left_children"], data["right_children"])
    traversals = get_traversals(tree)
    print(f"Tree {i} Traversals:")
    print(f"Preorder: {traversals['Preorder']}")
    print(f"Inorder: {traversals['Inorder']}")
    print(f"Postorder: {traversals['Postorder']}")
    print()