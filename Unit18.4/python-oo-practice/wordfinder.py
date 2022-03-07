"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """SWordFinder that takes in all the lines
    
    >>> wf = SpecialWordFinder("words1.txt")
    5 words read

    >>> swf.random() in ["Hello", "Bye", "CC", "DDAS", "planet"]
    True

    >>> swf.random() in ["Hello", "Bye", "CC", "DDAS", "planet"]
    True

    >>> swf.random() in ["Hello", "Bye", "CC", "DDAS", "planet"]
    True
    """

    def __init__(self, path):
        self.temp = open(path).readlines()
        self.lst = []
        for i in self.temp:
            self.lst.append(i.strip('\n'))
        print(f'{len(self.lst)} words read')

    def random(self):
        print(random.choice(self.lst))

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> wf = SpecialWordFinder("words2.txt")
    4 words read

    >>> swf.random() in ["parsnips", "apple", "kale", "mango"]
    True

    >>> swf.random() in ["parsnips", "apple", "kale", "mango"]
    True

    >>> swf.random() in ["parsnips", "apple", "kale", "mango"]
    True
    """
    def __init__(self, path):
        super().__init__(path)
        self.lst = []
        for i in self.temp:
            if i[0] != '' and i[0] != '\n' and i[0] != '#':
                self.lst.append(i.strip('\n'))
        print(f'{len(self.lst)} words read')
