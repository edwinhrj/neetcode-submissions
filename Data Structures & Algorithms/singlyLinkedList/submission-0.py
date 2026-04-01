class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # dummy node
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head # first is dummy node
        curr = curr.next # first numerical node!
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # index out of bounds
        

    def insertHead(self, val: int) -> None:
        curr = self.head # dummy node
        newNode = ListNode(val)
        newNode.next = curr.next
        curr.next = newNode

        # account for edge case where insert to empty LL
        if not newNode.next:
            self.tail = newNode


    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # and curr is used to ensure curr pointer is not empty
        # basically accounting for out of bounds index situation
        while i < index and curr: 
            # move curr to node before target node
            i += 1
            curr = curr.next

        if curr and curr.next:
            # account for case where removing last node, 
            # so need to update tail pointer
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
             
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
