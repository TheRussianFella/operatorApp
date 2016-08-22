from Element import Element

class Set:

    id = ""
    quant = 0
    elements = []

    def __init__(self, id, elements = []):
        self.id = id
        self.elements = elements

    def add(self, element):
        self.elements.append(element)

    def __getitem__(self, index):
        return self.elements[index]
