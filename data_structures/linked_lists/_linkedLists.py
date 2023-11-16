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
            