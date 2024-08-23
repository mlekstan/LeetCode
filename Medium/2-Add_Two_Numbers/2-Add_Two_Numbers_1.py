class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def __init__(self):
        #self.list1 = []
        #self.list2 = []
        self.x = True
        self.y = True
        self.m = 1
        self.suma1 = 0
        self.suma2 = 0

    
    def addTwoNumbers(self, l1, l2):
    
        if self.x == False:
            pass
        else:
            l1.val *= self.m
            self.suma1 += l1.val
            #self.list1.append(l1.val)
        
        if self.y == False:
            pass
        else:
            l2.val *= self.m
            self.suma2 += l2.val
            #self.list2.append(l2.val)
        
        
        if not l1.next and not l2.next:
            #suma = str(sum(self.list1) + sum(self.list2))
            suma = str(self.suma1 + self.suma2)
            list = []
            i = 0
            for digit in suma:
                try:
                    list.append(ListNode(int(digit), list[i]))
                    i += 1
                except Exception as e:
                    list.append(ListNode(int(digit), None))

            return list[-1]

        elif not l1.next:
            self.x = False
            l2 = l2.next
        elif not l2.next:
            self.y = False
            l1=l1.next
        else:
            l1 = l1.next
            l2 = l2.next
        
        self.m *= 10
        return self.addTwoNumbers(l1,l2)


node31 = ListNode(4)
node21 = ListNode(6, node31)
node11 = ListNode(5, node21)

node32 = ListNode(3)
node22 = ListNode(4, node32)
node12 = ListNode(2, node22)


x = Solution().addTwoNumbers(node11, node12)
print(x)

