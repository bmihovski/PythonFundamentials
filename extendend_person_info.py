name = input()
age = int(input())
town = input()
salary = float(input())
age_range = None
salary_range = None

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Town: {town}')
print(f'Salary: ${salary:.2f}')

if age < 18:
    age_range = 'teen'
elif 18 < age < 70:
    age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif 500 < salary < 2000:
    salary_range = 'medium'
else:
    salary_range = 'high'

print('Age range: ' + age_range)
print('Salary range: ' + salary_range)