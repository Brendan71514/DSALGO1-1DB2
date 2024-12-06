from LinkedBinaryTree import LinkedBinaryTree

# Equation 1: (3 * 5) - ((4 * 5) + (6 - 7))
tree1 = LinkedBinaryTree()
root1 = tree1._add_root('-')

left1 = tree1._add_left(root1, '*')
tree1._add_left(left1, 3)
tree1._add_right(left1, 5)

right1 = tree1._add_right(root1, '+')
left2 = tree1._add_left(right1, '*')
tree1._add_left(left2, 4)
tree1._add_right(left2, 5)

right2 = tree1._add_right(right1, '-')
tree1._add_left(right2, 6)
tree1._add_right(right2, 7)

print("Equation 1 Traversals:")
print("Preorder:", [p.element() for p in tree1.preorder()])
print("Inorder:", [p.element() for p in tree1.inorder()])
print("Postorder:", [p.element() for p in tree1.postorder()])

# Equation 2: ((a + b) * c) - (d - e)
tree2 = LinkedBinaryTree()
root2 = tree2._add_root('-')

left1 = tree2._add_left(root2, '*')
left2 = tree2._add_left(left1, '+')
tree2._add_left(left2, 'a')
tree2._add_right(left2, 'b')
tree2._add_right(left1, 'c')

right1 = tree2._add_right(root2, '-')
tree2._add_left(right1, 'd')
tree2._add_right(right1, 'e')

print("\nEquation 2 Traversals:")
print("Preorder:", [p.element() for p in tree2.preorder()])
print("Inorder:", [p.element() for p in tree2.inorder()])
print("Postorder:", [p.element() for p in tree2.postorder()])

# Equation 3: ((a ^ b) + (c + d)) + ((e * f) / (g + h))
tree3 = LinkedBinaryTree()
root3 = tree3._add_root('+')

left1 = tree3._add_left(root3, '+')
left2 = tree3._add_left(left1, '^')
tree3._add_left(left2, 'a')
tree3._add_right(left2, 'b')

right1 = tree3._add_right(left1, '+')
tree3._add_left(right1, 'c')
tree3._add_right(right1, 'd')

right2 = tree3._add_right(root3, '/')
left3 = tree3._add_left(right2, '*')
tree3._add_left(left3, 'e')
tree3._add_right(left3, 'f')

right3 = tree3._add_right(right2, '+')
tree3._add_left(right3, 'g')
tree3._add_right(right3, 'h')

print("\nEquation 3 Traversals:")
print("Preorder:", [p.element() for p in tree3.preorder()])
print("Inorder:", [p.element() for p in tree3.inorder()])
print("Postorder:", [p.element() for p in tree3.postorder()])

# Equation 4: (a + b) / (c * (d - (e ^ f)))
tree4 = LinkedBinaryTree()
root4 = tree4._add_root('/')

left1 = tree4._add_left(root4, '+')
tree4._add_left(left1, 'a')
tree4._add_right(left1, 'b')

right1 = tree4._add_right(root4, '*')
tree4._add_left(right1, 'c')

right2 = tree4._add_right(right1, '-')
left3 = tree4._add_left(right2, '^')
tree4._add_left(left3, 'e')
tree4._add_right(left3, 'f')
tree4._add_right(right2, 'd')

print("\nEquation 4 Traversals:")
print("Preorder:", [p.element() for p in tree4.preorder()])
print("Inorder:", [p.element() for p in tree4.inorder()])
print("Postorder:", [p.element() for p in tree4.postorder()])

# Equation 5: ((a - b) + c) * ((d + e) * (f / g))
tree5 = LinkedBinaryTree()
root5 = tree5._add_root('*')

left1 = tree5._add_left(root5, '+')
left2 = tree5._add_left(left1, '-')
tree5._add_left(left2, 'a')
tree5._add_right(left2, 'b')
tree5._add_right(left1, 'c')

right1 = tree5._add_right(root5, '*')
left3 = tree5._add_left(right1, '+')
tree5._add_left(left3, 'd')
tree5._add_right(left3, 'e')

right2 = tree5._add_right(right1, '/')
tree5._add_left(right2, 'f')
tree5._add_right(right2, 'g')

print("\nEquation 5 Traversals:")
print("Preorder:", [p.element() for p in tree5.preorder()])
print("Inorder:", [p.element() for p in tree5.inorder()])
print("Postorder:", [p.element() for p in tree5.postorder()])

# Equation 6: (a * (b + c)) + ((d + e) * (f / g))
tree6 = LinkedBinaryTree()
root6 = tree6._add_root('+')

left1 = tree6._add_left(root6, '*')
tree6._add_left(left1, 'a')

left2 = tree6._add_right(left1, '+')
tree6._add_left(left2, 'b')
tree6._add_right(left2, 'c')

right1 = tree6._add_right(root6, '*')

right2 = tree6._add_left(right1, '+')
tree6._add_left(right2, 'd')
tree6._add_right(right2, 'e')

right3 = tree6._add_right(right1, '/')
tree6._add_left(right3, 'f')
tree6._add_right(right3, 'g')

print("\nEquation 6 Traversals:")
print("Preorder:", [p.element() for p in tree6.preorder()])
print("Inorder:", [p.element() for p in tree6.inorder()])
print("Postorder:", [p.element() for p in tree6.postorder()])
