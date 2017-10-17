class Node:
    def __init__(self,value):
        self.data = value
        self.parent = 0
        self.left = 0
        self.right = 0
 
class List:
    def __init__(self):
        self.firstNode = Node(0) #root node

    def InsertLeft(self,aNode,aNewNode):
        aNewNode.parent = aNode
        aNode.left = aNewNode
 
    def InsertRight(self,aNode,aNewNode):
        aNewNode.parent = aNode
        aNode.right = aNewNode
 
    def InsertBeginning(self,aNewNode):
        aNewNode.parent = self.firstNode
        self.firstNode = aNewNode            

    def __printElement (self):
        print "\t\t\t %s " % (self.parent)
        print "\t %s " % (self.left)
        print "\t %s " % (self.right)
        
    def __ShowNodeData(self,aNode):
        print "parent: %s" % aNode.data
        if aNode.left != 0:
            print "left: %s" % (aNode.left.data)
            self.__ShowNodeData(aNode.left)
        if aNode.right != 0:
            print "right %s" % aNode.right.data
            self.__ShowNodeData(aNode.right)
 
    def Dump(self):
        self.__ShowNodeData(self.firstNode)


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
 
aTree = List()
 
aTree.InsertBeginning(nodeB)
aTree.InsertLeft(nodeB,nodeD)
aTree.InsertRight(nodeB,nodeC)
aTree.InsertRight(nodeC,nodeA)
 
aTree.Dump()
        