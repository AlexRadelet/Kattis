#LINKED LIST
#Chaque node pointe vers le suivant, le dernier pointe vers None
#Complexité O(n)
#Double linkded list : Les pointeurs vont dans les 2 directions (None reference au début aussi)
#Pratique quand on veut ajouter à la fin de la liste
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        #SI la liste est vide, head est None
        self.head = None
        #Si on ajoute un Node, head prendra sa valeur
        self.tail = None

    # O(n) - linear time
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"
            while last.next is not None:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"
            return return_string
    #O(n) - linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - Linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    #O(1) - Constant time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

    #O(1) - Constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    #O(n) - linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n) - linear time
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next :
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) - linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # O(n) - linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value


if __name__ == "__main__":
    ll = DoubleLinkedList()

    ll.append(10)
    ll.insert(5,1)

    ll.insert(20, 1)
    ll.insert(18, 1)
    ll.insert(22, 1)
    ll.insert(88, 1)
    ll.insert(97, 1)



    ll.prepend(100)

    ll.insert(200,1)
    ll.delete(18)
    ll.delete(22)
    ll.delete(5)

    ll.pop(1)

    print(ll)
    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)
