class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.root = False
        # would it be an idea to store the position for each element


class LinkedList:
    def __init__(self, initial_value=None):
        self.root_element = Element(value=initial_value)
        self.root_element.root = True

    def append(self, add_value):
        """adds a new link to the end of the linked list, takes a value
        parameter named add_value"""
        import pdb; pdb.set_trace()
        current = self.root_element
        while current.next:
            current = current.next
        current.next = Element(add_value)

    def get_position(self, position):
        if position == 1:
            return self.root_element
        else:
            current = self.root_element
            for i in range(position - 1):
                try:
                    current = current.next
                except AttributeError:
                    return None
                else:
                    return current

    def insert(self, new_element, position):
        pass

    def delete(self, value):
        pass

    # should have a str function that displays the values in the list
