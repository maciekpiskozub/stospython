class Stos:
    def __init__(self):
        self.zawartosc = []

    def push(self, zawartosc):
        self.zawartosc.append(zawartosc)

    def pop(self):
        return self.zawartosc.pop()

    def top(self):
        return self.zawartosc[-1]

    def is_empty(self):
        if len(self.zawartosc) == 0:
            return True
        else:
            return False