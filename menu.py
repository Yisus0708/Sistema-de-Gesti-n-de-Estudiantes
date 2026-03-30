from service import register_student, show_student, search_student, update_student, delete_student

def show_menu():
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Register student")
    print("2. Show student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

def execute(option):
    if option == "1":
        name_option = input("Student name: ").strip()
        age_option = input("Age: ").strip()
        course_option = input("Course: ").strip()
        status_option = input("Status: ").strip()
        register_student(name_option, age_option, course_option, status_option)

    elif option == "2":
        show_student()

    elif option == "3":
        criterion = input("Search by ID or name: ").strip()
        s = search_student(criterion)
        if s:
            print("ID: " + str(s["id"]))
            print("Name: " + s["name"])
            print("Age: " + str(s["age"]))
            print("Course: " + s["course"])
            print("Status: " + s["status"])
        else:
            print("Student not found D:")

    elif option == "4":
        criterion = input("Search by ID or name: ").strip()
        print("Leave blank if you don't want to update")
        name_new = input("New name:").strip() or None
        age_new = input(str("New year: ")).strip() or None
        course_new = input("New Course: ").strip() or None
        status_new = input("New Status (Active/Inactive): ").strip() or None
        update_student(criterion, name_new, age_new, course_new, status_new)

    elif option == "5":
        criterion = input("Search by ID or name: ").strip()
        delete_student(criterion)
        
    elif option == "6":
        return False
    
    else:
        print("Invalid option")
    return True  