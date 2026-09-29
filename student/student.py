class Student:
    def __init__(self, name, grade_level):

       self.name = name
       self.grade_level = grade_level

    def promote(self):
        if self.grade_level >= 1 and self.grade_level < 12:
            self.grade_level += 1
            return self.grade_level

        raise ValueError("Invalid grade")

    def has_passed(self, score):
        if(score < 0 or score > 100):
            raise ValueError("Invalid score")

        if score >= 50:
            return True

        return False

    def update_name(self, name):

        if(name == ""):
            raise ValueError("Invalid name")

        self.name = name
        return self.name

    def is_graduating(self):
        return self.grade_level == 12