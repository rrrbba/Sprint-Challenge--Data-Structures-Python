from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #check to see if storage is less than capacity
        if self.storage.length < self.capacity:
            #if so then add new item to tail
            self.storage.add_to_tail(item)
            #also update the current position
            self.current = self.storage.head

        #check if the storage has reached capacity
        elif self.storage.length == self.capacity:
            remove = self.storage.head
            
            #if so, remove the head to make room
            self.storage.remove_from_head()
            #now that there is room, add new item to tail
            self.storage.add_to_tail(item)

            if remove == self.current:
                #update current positon 
                self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #start off by setting current_node to the root
        current_node = self.current
        #add root to the list
        list_buffer_contents.append(current_node.value)

        # If there is a next node, set current mode to next
        if current_node.next:
            next_node = current_node.next

        #if no node
        else:
            next_node = self.storage.head

        # go through list
        while next_node != current_node:
            #add the value of the next node to the list
            list_buffer_contents.append(next_node.value)
            #if there is a next node, then next_node is set to it
            if next_node.next:
                next_node = next_node.next
            else:
             # once at the end, go back to the top
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
