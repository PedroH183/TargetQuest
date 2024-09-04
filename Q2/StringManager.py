class StringManager:
    def __init__(self, string : str):
        self.string = string

    def verifyContainsALetter(self):
        return self.string.upper().count('A')

s = StringManager("pedro henriqueA")
print(s.verifyContainsALetter())