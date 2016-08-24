from Bundle import Bundle

class Order:

    id = ""
    #sets = []
    bundles = {}

    def __init__(self, id, bundles = {}):
        self.id = id
        self.bundles = bundles

    def add(self, bundle):
        #self.sets.append(set)
        self.bundles[bundle.id] = bundle

    def __getitem__(self, index):
        return self.bundles[index]
