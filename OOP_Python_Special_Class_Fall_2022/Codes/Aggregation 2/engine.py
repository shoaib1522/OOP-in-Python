class Engine:
    def __init__(self, company, manual_automatic):
        self.company = company
        self.manual_automatic = manual_automatic

    def __str__(self):
        return f'Engine Company: {self.company}\tTransmission: {self.manual_automatic}'

    def __del__(self):
        print ('del function called for Engine')


