import json
def load_data(filename):
    students = {}
    with open(filename, 'r') as file:
        reader = json.load(file)
#En el jason file no se usa next
        
    for student_id, student_info in reader.items():
        student = student_info[0]
        name = student['name']
        grade = student['grade']
        group = student['group']
        students[student_id] = [name, grade, group]
    return students



def main():
    file_name = 'data.json'
    student_data = load_data(file_name)
    for student in student_data:
        print(f'Student Id: {student}')
        print(f'Student Name: {student_data[student][0]}')
        print(f'Student Grade:  {student_data[student][1]}')
        print(f'Student Group:  {student_data[student][2]}')
        print()
main()

#student es el index 0, sease los numeros, vaya