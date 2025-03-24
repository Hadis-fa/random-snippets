import csv

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(row[0], row[1])

# ----------------
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(student["name"], student["house"])


# sort by keys in the dictionary
def get_name(student):
    return student["name"]


# if you want to sort it by house you can create another function and change function you are assigning to the key
for student in sorted(students, key=get_name):
    print(student["name"], student["house"])

# to wrap up the code further
for student in sorted(students, key=lambda student: student["name"]):
    print(student["name"], student["house"])


# ---------------
students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


# when you changed the file and added name and homw at the top
#

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


# write data to a file
# you need to add name and home at the top of the file by urself
name = input("what's your name? ")
home = input("where's your home: ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# other way of doing
name = input("what's your name? ")
home = input("where's your home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})


