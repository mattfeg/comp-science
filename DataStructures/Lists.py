class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    @property
    def isEmpty(self):
        return self.head == None

    @property
    def _lastElement(self):
        currentElement = self.head
        while currentElement.next != None:
            currentElement = currentElement.next
        return currentElement

    def __len__(self):
        if self.isEmpty:
            return 0
        currentElement = self.head
        count = 1
        while currentElement.next != None:
            count += 1
            currentElement = currentElement.next
        return count

    def __getitem__(self, index):
        if self.isEmpty:
            return
        currentElement = self.head
        for i in range(index):
            if currentElement.next == None:
                return
            currentElement = currentElement.next
        return currentElement.value

    def __setitem__(self, index, value):
        if self.isEmpty:
            return
        currentElement = self.head
        for i in range(index):
            if currentElement.next == None:
                return
            currentElement = currentElement.next
        currentElement.value = value

    def __delitem__(self, index):
        if self.isEmpty:
            return
        if index == 0:
            self.head = self.head.next
            return
        currentElement = self.head
        for i in range(index-1):
            if currentElement.next == None:
                return
            currentElement = currentElement.next
        currentElement.next = currentElement.next.next

    def append(self,value):
        if self.isEmpty:
            self.head = Element(value)
            return
        self._lastElement.next = Element(value)
    
    def pop(self):
        if self.isEmpty:
            return
        if self.head.next == None:
            self.head = None
        currentElement = self.head
        while currentElement != None:
            if currentElement.next.next == None:
                currentElement.next = currentElement.next.next
                return
            currentElement = currentElement.next
        
    def print(self):
        if self.head == None:
            return print("Empty List!")
        currentElement = self.head
        while currentElement.next != None:
            print(currentElement.value)
            currentElement = currentElement.next
        print(currentElement.value)
            