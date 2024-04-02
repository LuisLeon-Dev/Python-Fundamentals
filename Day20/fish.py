from animal import Animal


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("Moving in water")
