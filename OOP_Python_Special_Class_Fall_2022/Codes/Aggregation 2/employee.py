from address import *

class Employee:
    def __init__(self, name, designation, h_no, st_no, town, city, salary):
        self.e_name = name
        self.designation = designation
        self.c_address = Address(h_no, st_no, town, city)
        self.p_address = self.c_address
        self.salary = salary

    def __str__(self):
        s = f'Employee Name: {self.e_name}\nDesignation: {self.designation}\n'
        s += f'Current Address: {self.c_address}\n'
        if self.c_address == self.p_address:
            s += f'Permanent Address: Same as above\n'
        else:
            s += f'Permanent Address: {self.p_address}\n'
        return s + f'Salary: {self.salary}'

    def change_current_address(self, h_no, st_no, town, city):
        self.c_address = Address(h_no, st_no, town, city)
    def __del__(self):
        print (f'del function called for Employee')

def main():
    e1 = Employee('Asad Ali', 'Cashier', 23, 'A2', 'ABC Town', 'City XYZ', 30000)
    print(e1)
    print ('------------------------')
    e1.change_current_address(25, 'B5', 'ABC Town', 'City XYZ')
    print(e1)
main()
