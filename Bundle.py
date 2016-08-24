from Element import Element

class Bundle:

    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.elements = list()

    def add(self, element):
        self.elements.append(element)

    def __getitem__(self, index):
        return self.elements[index]

    def length(self):
        return len(self.elements)
