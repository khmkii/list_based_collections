class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.root = False


class LinkedList:
    def __init__(self, initial_value=None):
        self.root_element = Element(value=initial_value)
        self.root_element.root = True

    def append(self, add_value):
        """
        adds a new link to the end of the linked list, takes a value
        parameter named add_value
        """

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

    def insert(self, new_element_value, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        """

        if position == 1:
            self.root_element.root = False
            self.root_element = Element(new_element_value)
            self.root_element.root = True
        else:
            posterior = self.get_position(position)
            if posterior is not None:
                new_element = Element(new_element_value)
                prior = self.get_position(position-1)
                new_element.next = posterior
                prior.next = new_element
            else:
                raise IndexError(
                        "cannot insert outside of the linked list, try append instead"
                    )

    def delete(self, value):
        pass
