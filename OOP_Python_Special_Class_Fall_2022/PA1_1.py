class Instructor:
    def __init__(self, fname, lname, office_no):
        self.fname = fname
        self.lname = lname
        self.office_no = office_no
    def __str__(self):
        return f'{self.fname} {self.lname} {self.office_no} '

class Classroom:
    def __init__(self, building_no, room_no):
        self.building_no = building_no
        self.room_no = room_no
    def __str__(self):
        return f'{self.building_no} {self.room_no} '

class CollegeCourse:
    def __init__(self, fname, lname, office_no, building_no, room_no, credits):
        self.instructor = Instructor (fname, lname, office_no)
        self.classroom = Classroom (building_no, room_no)
        self.credits = credits
    def __str__(self):
        return f'Instructor: {str(self.instructor)}\nClass Room: {str(self.classroom)}\nCredits: {str(self.credits)}'
    
def main():
    course1 = CollegeCourse('Asad', 'Khan', 15, 'Building A', 34, 3)
    course2 = CollegeCourse('Saad', 'Jamil', 17, 'Building B', 13, 4)
    course3 = CollegeCourse('Haris', 'Sheikh', 20, 'Building A', 28, 3)
    print(course1)
    print(course2)
    print(course3)

main()
