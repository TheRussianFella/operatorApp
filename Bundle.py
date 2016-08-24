from Element import Element

class Bundle:

    id = ""
    name = ""
    quantity = 0
    elements = []

    def __init__(self, id, name, quantity, elements = []):
        self.id = id
        self.elements = elements
        self.name = name
        self.quantity = quantity

    def add(self, element):
        self.elements.append(element)

    def __getitem__(self, index):
        return self.elements[index]

    def length(self):
        return len(self.elements)
