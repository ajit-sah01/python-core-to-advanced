from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: int

e1 = Employee("Ajit", 50000)
e2 = Employee("Nilam", 50000)
print(e1)
print(e2)
