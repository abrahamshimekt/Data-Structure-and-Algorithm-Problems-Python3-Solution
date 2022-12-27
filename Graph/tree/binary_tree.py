class BinaryTreeNode(object):
    def __init__(self):
        self.data = "#"
        self.leftChild = None
        self.rightChild = None
class BinaryTRee:
    def creatBinaryTree(self,root):
        data = input('==>')
        if data == "#":
            root = None
        else:
            root.data = data
            root.leftChild = BinaryTreeNode()
            self.creatBinaryTree(root.leftChild)
            root.rightChild = BinaryTreeNode()
            self.creatBinaryTree(root.rightChild)
    def preorder(self,root):
        if root:
            self.visitBinaryTreeNode(root)
            self.visitBinaryTreeNode(root.leftChild)
            self.visitBinaryTreeNode(root.rightChild)
    def inorder(self,root):
        self.visitBinaryTreeNode(root.leftChild)
        self.visitBinaryTreeNode(root)
        self.visitBinaryTreeNode(root.rightChild)
    def postorder(self,root):
        self.visitBinaryTreeNode(root.leftChild)
        self.visitBinaryTreeNode(root.rightChild)
        self.visitBinaryTreeNode(root)




