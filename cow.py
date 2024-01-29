# provides definitions used in the cowsay file
class Cow:  # class Cow contains all methods for cow related functions
    def __init__(self, name):  # initializes cow object
        self.name = name
        self.image = None
    def get_name(self):  # provides name for cow
        if self.name is None:
            return "Unnamed Cow"
        else:
            return self.name

    def get_image(self):  # provides image for cow
        if self.image is None:
            return "No image available"
        else:
            return self.image

    def set_image(self, image):  # sets the image
        self.image = image

