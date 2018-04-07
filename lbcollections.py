class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.root = False

    def __str__(self):
        return self.value

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
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.
        """
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
        """
        Delete the first node with a given value.
        """
        if self.root_element.value == value:
            self.root_element = self.root_element.next
            self.root_element.root = True
        else:
            position = 2
            next_element = self.root_element.next
            while next_element:
                if next_element.value == value:
                    prior_element = self.get_position(position - 1)
                    after_element = self.get_position(position + 1)
                    prior_element.next = after_element
                    next_element.next = None
                else:
                    position += 1
                    continue



    # leverage del to remove position at index? or delete_at_position
