# class Tree:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Tree(data)
#                 else:
#                     self.left.insert(data)
#             else:
#                 if self.right is None:
#                     self.right = Tree(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     def printTree(self):
#         if self.left:
#             self.left.printTree()
#         print(self.data)
#         if self.right:
#             self.right.printTree()
#     """In order traversal of tree: The traversal method is implemented by creating
#     an empty list and adding the left node first followed by the root or the parent node.
#     """
#     def inorderTraversal(self,root):
#         res= []
#         if root:
#             res = self.inorderTraversal(root.left)
#             res.append(root.data)
#             res = res + self.inorderTraversal(root.right)
#         return res
#     """
#     Pre Order Traversal of  Tree: This implemented by creating an empty list and adding the root
#     node first followed by the left subtree and finally the right subtree
#     """
#     def preOrderTraversal(self,root):
#         res = []
#         if root:
#             res.append(root.data)
#             res = res + self.preOrderTraversal(root.left)
#             res = res + self.preOrderTraversal(root.right)
#         return res
#     """Post order traversal of Tree: Implemented by creating an empty list and adding the left subtree first
#     and followed by adding the right subtree finally the root node.
#     """
#     def postOrderTraversal(self,root):
#         res = []
#         if root:
#             res = self.postOrderTraversal(root.left)
#             res = res + self.postOrderTraversal(root.right)
#             res.append(root.data)
#         return res
#
#
#
#
#
#
#
# root = Tree(20)
# root.insert(30)
# root.insert(12)
# root.insert(32)
# root.insert(0)
# print(root.inorderTraversal(root))
# print(root.preOrderTraversal(root))
# print(root.postOrderTraversal(root))
#
#
#
print(ord("A"))
