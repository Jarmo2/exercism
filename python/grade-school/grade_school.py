from collections import defaultdict


class School:
    def __init__(self):
        self.students_in_grades = defaultdict(set)
        self.add_status = []

    def add_student(self, name: str, grade: int) -> None:
        student_to_add = not any(name in sublist for sublist in self.students_in_grades.values())
        if student_to_add:
            self.students_in_grades[grade].add(name)
        self.add_status.append(student_to_add)

    def roster(self) -> list[str]:
        return [student for grade in sorted(self.students_in_grades) for student in sorted(self.students_in_grades[grade])]

    def grade(self, grade_number: int) -> list[str]:
        return sorted(self.students_in_grades[grade_number])

    def added(self) -> list[bool]:
        return self.add_status
