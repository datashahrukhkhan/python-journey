class Camera:
    def take_photo(self):
        print("Photo captured")


class Phone:
    def make_call(self):
        print("Calling...")


class Smartphone(Camera, Phone):
    pass


mobile = Smartphone()
mobile.take_photo()
mobile.make_call()