from Set import Set

class Order:

    id = ""
    sets = []

    def __init__(self, id, sets = []):
        self.id = id
        self.sets = sets

    def add(self, set):
        self.sets.append(set)

    def __getitem__(self, index):
        return self.sets[index]
