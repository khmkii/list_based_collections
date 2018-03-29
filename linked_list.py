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

        current = self.root_element
        while current.next:
            current = current.next
        current.next = Element(add_value)

    def get_position(self, position):
        if isinstance(position, int):
            if position >= 1:
                current = self.root_element
                for i in range(0, position - 1):
                    current = current.next
                    if current is None:
                        return None
                return current 
            else:
                raise ValueError(
                    "position must be an integer greater than zero"
                )
        else:
            raise TypeError("position must be an integer")

    def insert(self, new_element, position):
        pass

    def delete(self, value):
        pass

    # should have a str function that displays the values in the list
