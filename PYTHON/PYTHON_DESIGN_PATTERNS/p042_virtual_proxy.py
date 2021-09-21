# proxy appears like actual object

class BitMap:
    def __init__(self, filename):
        self.filename = filename
        print(f"loading image from file {filename}")

    def draw(self):
        print(f"drawing image {self.filename}")


class LazyBitMap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = BitMap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print(f"about to draw image")
    image.draw()
    print(f"done drawing image")


if __name__ == "__main__":
    bmp = LazyBitMap("p042.jpg")
    draw_image(bmp)
