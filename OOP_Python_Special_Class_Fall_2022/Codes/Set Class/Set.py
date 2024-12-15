class Set:
    def __init__(self):
        self.__elements = []

    def element_not_exist(self, element):
        for c_element in self.__elements:
            if element == c_element:
                return False
        return True

    def add_element(self, element):
        if self.element_not_exist(element):
            self.__elements.append(element)

    def add_set(self, set2):
        for element in set2.__elements:
            if self.element_not_exist(element):
                self.__elements.append(element)

    def __str__(self):
        s = ''
        for element in self.__elements:
            s = s + str(element) + ' '
        return s
