from cow import Cow

class FileCow(Cow):  # creates a class for the new cows pulled from the zipped files
    def __init__(self, name, filename):
        super().__init__(name)
        try:
            with open(filename, 'r') as file:  # opens the file for reading
                self.image = file.read()  # reads the image
        except Exception as e:
            raise RuntimeError("MOOOOO!!!!!!") from e  # if the previous try does not work

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow Image")  # raises the runtime error