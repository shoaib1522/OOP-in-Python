class Address:
    def __init__(self, house_no, street_no, town, city):
        self.house_no = house_no
        self.street_no = street_no
        self.town = town
        self.city = city

    def __str__(self):
        return f'House No: {self.house_no}\tStreet No: {self.street_no}\tTown: {self.town}\tCity: {self.city}'

    def __del__(self):
        print ('del function called for Address')


