NAME = 'name'
GRADE = 'grade'


class School:
    def __init__(self):
        self.students = []
        self.add_status = []

    def add_student(self, name: str, grade: int) -> None:
        if len(self.students) == 0:
            self.students.append(
            {NAME: name,
            GRADE: grade}
        )
            self.add_status.append(True)
        else:
            if all(d[NAME] != name or d[NAME] != name and d[GRADE] != grade for d in self.students):
                self.students.append(
                {NAME: name,
                 GRADE: grade}
            )
                self.add_status.append(True)
            else:
                self.add_status.append(False)

    def roster(self) -> list[str]:
        sorted_students = sorted(self.students, key=lambda k: (k['grade'], k['name']))
        return [student[NAME] for student in sorted_students]

    def grade(self, grade_number: int) -> list[str]:
        return sorted([student[NAME] for student in self.students if student[GRADE] == grade_number])

    def added(self) -> list[bool]:
        return self.add_status
