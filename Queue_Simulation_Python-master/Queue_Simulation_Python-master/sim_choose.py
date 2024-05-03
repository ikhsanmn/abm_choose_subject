import random

class Subject:
    def __init__(self, name, time, value):
        self.name = name
        self.time = time
        self.value = value

class Student:
    def __init__(self, name, max_time):
        self.name = name
        self.max_time = max_time
        self.subjects = []

    def choose_subject(self, available_subjects):
        possible_subjects = [subject for subject in available_subjects if subject.time <= self.max_time and subject not in self.subjects] #part of subject must same
        if not possible_subjects:
            return None
        return random.choice(possible_subjects)

class College:
    def __init__(self):
        self.subjects = []
        self.students = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_student(self, student):
        self.students.append(student)

    def run_simulation(self):
        for student in self.students:
            while student.max_time > 0:
                chosen_subject = student.choose_subject(self.subjects)
                if chosen_subject:
                    student.subjects.append(chosen_subject)
                    student.max_time -= chosen_subject.time
                else:
                    break

# Creating subjects
subjects_data = [
    {"name": "Math", "time": 4, "value": 3},
    {"name": "Physics", "time": 3, "value": 3},
    {"name": "Biology", "time": 3, "value": 3},
    {"name": "History", "time": 2, "value": 2},
    {"name": "Art", "time": 2, "value": 2}
]

subjects = [Subject(sub["name"], sub["time"], sub["value"]) for sub in subjects_data]

# Creating students
students_data = [
    {"name": "Alif", "max_time": 10},
    {"name": "Boby", "max_time": 12},
    {"name": "Charles", "max_time": 8},
    {"name": "Dani", "max_time": 11},
    {"name": "Eva", "max_time": 9}
]

students = [Student(student["name"], student["max_time"]) for student in students_data]

# Creating a college
college = College()

# Adding subjects and students to the college
for subject in subjects:
    college.add_subject(subject)

for student in students:
    college.add_student(student)

# Running the simulation
college.run_simulation()

# Printing the results
for student in students:
    print(f"{student.name} chose the following subjects:")
    for subject in student.subjects:
        print(f"- {subject.name} (Time: {subject.time}, Value: {subject.value})")
