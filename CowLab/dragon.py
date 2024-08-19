from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(name)
        self.image = image
    def can_breathe_fire(self):
        return True