from Bundle import Bundle

class Order:

    def __init__(self, id):
        self.id = id
        self.bundles = dict()

    def add(self, bundle):
        #self.sets.append(set)
        self.bundles[bundle.id] = bundle

    def __getitem__(self, index):
        return self.bundles[index]
