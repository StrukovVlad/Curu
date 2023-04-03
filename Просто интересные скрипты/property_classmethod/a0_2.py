class Employee:
    pass


class EmployeeToDemoInit(Employee):
    next_employee_id = 1
    BASE_PAY = 1000
    LIST_OF_SKILLS_REQUIRED = 'java'

    def __init__(self, name, years_of_experience, skill, location):
        self.name = name
        self.years_of_experience = years_of_experience
        self.__skill = skill
        self.location = location
        self.employee_id = EmployeeToDemoInit.next_employee_id
        EmployeeToDemoInit.next_employee_id += 1

    def calculate_employee_bonus(self):
        return EmployeeToDemoInit.BASE_PAY + EmployeeToDemoInit.BASE_PAY * .3

    @staticmethod
    def _calculate_bonus_on_base_pay():
        return EmployeeToDemoInit.BASE_PAY * .15

    @classmethod
    def create_empoyee_with_location(cls):
        return cls.BASE_PAY, cls.LIST_OF_SKILLS_REQUIRED, cls.next_employee_id

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        if value not in EmployeeToDemoInit.LIST_OF_SKILLS_REQUIRED:
            raise ValueError('Skills do no match')
        self.__skill = value


emp = EmployeeToDemoInit('Vlad','one','Pythonist','India')

# print(emp.calculate_employee_bonus())
# # 1300.0
# print(EmployeeToDemoInit.create_empoyee_with_location())
# # Vlad, one, Pythonist, location='India'
# print(emp._calculate_bonus_on_base_pay())
# # 150.0
print(emp.skill)
# Pythonist
emp.skill = 'java'
print(emp.skill)
# java
emp.skill = 'php'
print(emp.skill)
# ValueError: Skills do no match