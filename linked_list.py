class Linked_List:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self._head = new_node
        self._tail = new_node
        self._length = 1

    def print_list(self) -> None:
        current_node = self._head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            return None
        temp = self._head
        pre = self._head
        while(temp.next):
            pre = temp
            temp = temp.next
        self._tail = pre
        self._tail.next = None
        self._length -= 1
        if self._length == 0:
            self._head = None
            self._tail = None
        return temp.value

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self.head
            self._head = new_node
        self._length += 1
        return True

    def pop_first(self):
        if self._head is None:
            return None
        temp = self._head
        self._head = self._head.next
        temp.next = None
        self._length -= 1
        if self._length == 0:
            self._tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


     
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
