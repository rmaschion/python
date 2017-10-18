
def reverseString(strIN):
    #new string to return result
    newStr = []
    for i in strIN[::-1]:
        newStr.append(i)
    return ''.join(newStr)

def reverseWithSwap(a): #O(n)
    index = len(a)-1
    secondSegment = firstSegment = ""
    half = len(a)/2
    for i in range(0,half):
        firstSegment += a[index]
        secondSegment += a[half-i-1]
        index -= 1
    return firstSegment + secondSegment


    #startNumber = int(raw_input("Enter the start number here "))
    #endNumber = int(raw_input("Enter the end number here "))

if __name__ == '__main__':
    print "%sreverseString%s" % ("*" * 30,"*" * 30)
    print reverseString("12345678")
    print "%sreverseWithSwap%s" % ("*" * 30,"*" * 30)
    print reverseWithSwap("12345678")

