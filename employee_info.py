import random

f_name = ["John", "Jordan", "Blake", "Drew", "Jerome", "Sunny", "Jack", "Richard"]
l_name = ["King", "Smith", "Longbottom", "Singh", "Xi", "Natsuki", "Joestar", "Brando"]
for i in range(1, 7):
    print(f"INSERT INTO employee_info(id, f_name, l_name, age) VALUES ({i}, \'{f_name[random.randint(0,7)]}\', "
          f"\'{l_name[random.randint(0,7)]}\', {random.randint(20,100)});")

jobs = ["Janitor", "Team Member", "Manager"]

for i in range(1, 7):
    print(f"UPDATE employee_info\nSET job = \"{jobs[random.randint(0,2)]}\"\nWHERE id = {i}; ")