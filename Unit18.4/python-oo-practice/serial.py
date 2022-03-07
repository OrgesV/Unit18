"""Python serial number generator."""

class SerialGenerator:
    check = 10
    def __init__(self, start):
        self.start = start - 1
        self.temp = start - 1
    def generate(self):
        self.start += 1
        return self.start
    def reset(self):
        self.start = self.temp
    print(f'{check}")
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
