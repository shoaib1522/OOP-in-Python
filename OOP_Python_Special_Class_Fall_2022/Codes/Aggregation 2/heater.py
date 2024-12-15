class Heater:
    def __init__(self, company, size):
        self.company = company
        self.size = size

    def __str__(self):
        return f'Heater Company: {self.company}\tHeater Size: {self.size}'

    def __del__(self):
        print ('del function called for Heater')


