from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def can_breathe_fire(self):  # cannot breathe fire
        return False
