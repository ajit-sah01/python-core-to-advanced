import numpy as np

dtype = np.dtype([
    ('name', 'U10'),
    ('age', 'i4'),
    ('salary', 'f4')
])

employees = np.array([
    ('Ajit', 20, 50000.0),
    ('Rahul', 22, 60000.0),
    ('Nilam', 21, 55000.0)
], dtype=dtype)

print(employees)

# Access fields
print(employees['name'])
print(employees['salary'])

# Filter data
high_salary = employees[employees['salary'] > 55000]
print(high_salary)