#Function to reverse the linked list

class Solution(object):
    def reverseList(self, head):
            curr = head
            prev = None

            while(curr != None):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return(prev)

class node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Function to print the elements in linked list
def printlist(n):
    init = n
    print(n.val)
    n = n.next
    while(n != init and n):
        print(n.val)
        n = n.next
    
# Linked list creation
list = [1,2,3,4,5]
head = node(list[0])

curr = head
for i in range(1,len(list)):
    curr.next = node(list[i])
    curr = curr.next


# Call function to reverse the list
new_solution = Solution()
head = new_solution.reverseList(head)

printlist(head)
