class Tyre:
    def __init__(self, company, size):
        self.company = company
        self.size = size

    def __str__(self):
        return f'Tyre Company: {self.company}\tTyre Size: {self.size}'

    def __del__(self):
        print ('del function called for Tyre')


