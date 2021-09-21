# expose multiple components through single interface

class Buffer:
    def __init__(self, width=10, height=2):
        self.width = width
        self.height = height
        self.buffer = [" "] * (width*height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class ViewPort:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer += text


# facade
class Console:
    def __init__(self):
        b = Buffer()
        self.current_view_port = ViewPort(b)
        self.buffers = [b]
        self.viewports = [self.current_view_port]

    def write(self, text):
        self.current_view_port.buffer.write(text)

    def get_char_at(self, index):
        return self.current_view_port.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("neha")
    print(c.get_char_at(-1))
