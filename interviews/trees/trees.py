# A binary ordered tree example

class CNode:
    left, right, data = None, None, 0

    def __init__(self, data):
        # initializes the data members
        self.left = None
        self.right = None
        self.data = data


class CBOrdTree:
    def __init__(self):
        # initializes the root member
        self.root = None

    def addNode(self, data):
        # creates a new node and returns it
        return CNode(data)

    def insert(self, root, data):
        # inserts a new data
        if root == None:
            # it there isn't any data
            # adds it and returns
            return self.addNode(data)
        else:
            # enters into the tree
            if data <= root.data:
                # if the data is less than the stored one
                # goes into the left-sub-tree
                root.left = self.insert(root.left, data)
            else:
                # processes the right-sub-tree
                root.right = self.insert(root.right, data)
            return root

    def lookup(self, root, target):
        # looks for a value into the tree
        if root == None:
            return 0
        else:
            # if it has found it...
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    # left side
                    return self.lookup(root.left, target)
                else:
                    # right side
                    return self.lookup(root.right, target)

    def minValue(self, root):
        # goes down into the left
        # arm and returns the last value
        while (root.left != None):
            root = root.left
        return root.data

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            # computes the two depths
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            # returns the appropriate depth
            return max(ldepth, rdepth) + 1

    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def printTree(self, root):
        # prints the tree path
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print root.data,
            self.printTree(root.right)

    def printRevTree(self, root):
        # prints the tree path in reverse
        # order
        if root == None:
            pass
        else:
            self.printRevTree(root.right)
            print root.data,
            self.printRevTree(root.left)


if __name__ == "__main__":
    # create the binary tree
    BTree = CBOrdTree()
    # add the root node
    root = None
    # ask the user to insert values
    for i in range(0, 5):
        data = int(raw_input("insert the node value nr %d: " % i))
        # insert values
        if root:
            BTree.insert(root, data)
        else:
            root = BTree.addNode(data)

    print "\n"

    print "\nprint tree"
    BTree.printTree(root)

    print "\nprint reverse tree"
    BTree.printRevTree(root)

    data = int(raw_input("\n\ninsert a value to find: "))
    if BTree.lookup(root, data):
        print "\nfound"
    else:
        print "\nnot found"

    print "\nprint min value"
    print BTree.minValue(root)

    print "\nprint max depth"
    print BTree.maxDepth(root)

    print "\nprint tree's size"
    print BTree.size(root)
