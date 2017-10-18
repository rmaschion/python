def fiboNotRecursive(n):
    a, b = 0, 1

    while n:
        n -= 1
        a, b = b, a + b
        print a,


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


def countOdd(l):
    if not l: return 0
    count = 0
    if l[0] % 2:
        count += 1
        # print count
        # print l[0]
    count += countOdd(l[1:])
    return count


# print countOdd([1,2,3,4,5,6,7,8,9])

def printOdds(n):
    for i in range(0, n):
        if i % 2 == 0:
            print "odds: %s" % i


import sys


# printOdds(5)

class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = 0


class linkedList:
    def __init__(self):
        self.firstNode = Node(0)

    def __showData(self, node):
        if (node.next != 0):
            print node.data
            self.__showData(node.next)

    def InsertBeginning(self, node):
        node.next = self.firstNode
        self.firstNode = node

    def InsertAfter(self, node, newNode, ):
        newNode.next = node.next
        node.next = newNode

    def Dump(self):
        self.__showData(self.firstNode)


# nodeA = Node("A")
# nodeB = Node("B")
# nodeC = Node("C")
# nodeD = Node("D")

# aList = linkedList()


# aList.InsertBeginning(nodeB)
# aList.InsertAfter(nodeB,nodeD)
# aList.InsertAfter(nodeD,nodeC)
# aList.InsertAfter(nodeC,nodeA)

# aList.Dump()


def reverseString(strIN):
    newStr = []
    for i in strIN[::-1]:
        newStr.append(i)
    return ''.join(newStr)


# print reverseString("this is a string")

    #startNumber = int(raw_input("Enter the start number here "))
    #endNumber = int(raw_input("Enter the end number here "))

if __name__ == '__main__':

    print "%sfiboNotRecursive%s" % ("*" * 30,"*" * 30)
    for f in xrange(10):
        fiboNotRecursive(f)
        print

    print "%sfiboRecursive%s" % ("*" * 30, "*" * 30)
    print map(fib, range(1,10))