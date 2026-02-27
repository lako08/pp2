class Reverse:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= 0:
            result = self.text[self.index]
            self.index -= 1
            return result
        else:
            raise StopIteration

s = input()

reverse_iter = Reverse(s)

for char in reverse_iter:
    print(char, end='')