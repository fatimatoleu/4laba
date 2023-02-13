#2.	Напишите программу, в которой предлагается вводить учащихся различных груп, посещающих секции по программированию. 
# Требуется упорядочить список по возрастанию классов. Распечатать список фамилий и классов. 
students = []

while True:
    group = input("Введите название группы (или нажмите Enter для завершения): ")
    if group == '':
        break
    while True:
        student = input("Введите имя учащегося (сначала фамилию) и класс, разделенные запятой (или нажмите Enter для завершения): ")
        if student == '':
            break
        last_name, cls = student.split(',')
        students.append((last_name.strip(), int(cls.strip())))

students.sort(key=lambda x: x[1])

print("Список фамилий и классов: ")
for student in students:
    print(f"{student[0]}: Class {student[1]}")
