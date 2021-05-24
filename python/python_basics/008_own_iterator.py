class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        print("iter")
        # make an iterable
        # i.e. return an object which has __next__ method i.e. itself in this case
        return self

    def __next__(self):
        print("next")
        # makes an iterator
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

my_sentence = Sentence("my name is smita")
print(dir(my_sentence))
for word in my_sentence:
    print(word)