import student

def register_student(name_student,age_student,course_student,status_student="active"):
    data_student= {
        "id": student.student_id,
        "name": name_student,
        "age": age_student,
        "course": course_student,
        "status": status_student
    }

    student.student_counter.append(data_student)
    student.student_id = student.student_id + 1
    print(f"Student registered with ID uwu: " + str(data_student["id"]))

def show_student():
    if not student.student_counter:
        print("There are no students registered :(")
        return
    print("\n ID | Name Student | Age | Course | Status ")
    print("-" * 45)
    for s in student.student_counter:
        print(str(s["id"]) + "|" + s["name"] + "|" + s["age"] + "|" + s["course"] + "|" + s["status"])
    print("-" * 45)
    
def search_student(criterion):
    for s in student.student_counter:
        if str(s["id"]) == str(criterion) or s["name"].lower() == criterion.lower():
            return s
    return None

def update_student(criterion,new_name=None,new_age=None,new_course=None,new_status=None):
    s = update_student(criterion)
    if s is None:
        s["name"] = new_name
    if s is None:
        s["age"] = new_age
    if s is None:
        s["course"] = new_course
    if s is None:
        s["status"] = new_status
    print("Student successfully updated :D")

def delete_student(criterion):
    s = search_student(criterion)
    if s is None:
        print("Student not found")
        return
    student.student_counter.remove(s)
    print("Student eliminated :)")

    