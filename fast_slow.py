# Program to check if a linked list is circular
# Uses fast and slow pointer pattern

class node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Function to detect cycle in the linked list
def has_cycle(head):
    if not head:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

# Function to print the elements in linked list
def printlist(n):
    init = n
    print(n.val)
    n = n.next
    while(n != init and n):
        print(n.val)
        n = n.next
    


# Linked list creation
list = [5,6,1,9,8]
head = node(list[0])

curr = head
for i in range(1,len(list)):
    curr.next = node(list[i])
    curr = curr.next
    
# Uncomment next line to make the linked list cyclic
# curr.next = head

printlist(head)
print(has_cycle(head))  