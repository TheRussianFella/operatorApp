from PIL import Image

class Element:

    def __init__(self, id, name, quantity, frontPic, backPic, contentPic):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.frontPick = frontPic
        self.backPick = backPic
        self.contentPic = contentPic
