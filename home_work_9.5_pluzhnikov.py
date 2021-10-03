class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Handle(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} handle!")


stat = Stationery()
pen = Pen("Parker")
pencil = Pencil("Palamino")
handle = Handle("Ciao")

office_supplies = [stat, pen, pencil, handle]

for i in office_supplies:
    i.draw()