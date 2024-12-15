from functions import *
class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities
    def __str__(self):
        s = 'RENTAL DETAILS\n'
        s += 'rent: {}'.format(self.rent)
        s += '\nestimated utilities: {}'.format(self.utilities)
        s += '\nfurnished: {}'.format(self.furnished)
        return s
    def set_values(self):
        self.rent=input('What is the monthly rent? ')
        self.utilities=input('What are the estimated utilities? ')
        self.furnished = get_valid_input('Is the property furnished? ', ('yes', 'no'))
    def prompt_init():
        return dict(rent=input("What is the monthly rent? "), utilities=input("What are the estimated utilities? "), furnished = get_valid_input("Is the property furnished? ", ("yes", "no")))

    prompt_init = staticmethod(prompt_init)

